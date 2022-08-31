from django.views.generic import ListView, DetailView
from cart.forms import AddToCartForm
from rest_framework import views, permissions, status
from .models import Production, Category
from .serializers import ProductionSerializer, CategorySerializer
from rest_framework.response import Response


class CategoryDetailView(DetailView):
    model = Category
    slug_url_kwarg = 'category_slug'
    template_name = "#"

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)

        products = Production.objects.filter(
            category=self.get_object()
        ).prefetch_related('image')

        context.update({
            'products': products
        })
        return context


class ProductsListView(ListView):
    model = Production
    queryset = Production.objects.all().active().prefetch_related('image')
    template_name = "#"


class ProductDetailView(DetailView):
    model = Production
    template_name = "#"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['form'] = AddToCartForm
        return context


class ProductionListAPI(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated(), permissions.IsAdminUser()]
        return [permissions.AllowAny()]

    def get(self, request):
        serializer = ProductionSerializer(
            Production.objects.all(),
            context={'request': request},
            many=True)
        return Response(data={
            'data': serializer.data,
            'message': 'Production retrieved successfully.'
        })

    def post(self, request):
        serializer = ProductionSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(data={
                'data': serializer.data,
                'message': 'Production created successfully.'
            }, status=status.HTTP_201_CREATED)
        return Response(data={
            'data': serializer.errors,
            'message': 'Production creation failed.',
            'error': True
        }, status=status.HTTP_400_BAD_REQUEST)


class CategoryListAPI(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated(), permissions.IsAdminUser()]
        return [permissions.AllowAny()]

    def get(self, request):
        serializer = CategorySerializer(Category.objects.all(), many=True)
        return Response(data={
            'data': serializer.data,
            'message': 'Category retrieved successfully.'
        })

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={
                'data': serializer.data,
                'message': 'Category created successfully.'
            }, status=status.HTTP_201_CREATED)
        return Response(data={
            'data': serializer.errors,
            'message': 'Category creation failed.',
            'error': True
        }, status=status.HTTP_400_BAD_REQUEST)
