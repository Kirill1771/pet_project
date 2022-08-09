from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from candy_shop_app.models import Production, Category
from .permissions import IsAdminOrReadOnly
from .serializers import ProductionSerializer, CategorySerializer


class CandyShopAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ProductionAPIList(generics.ListCreateAPIView):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = CandyShopAPIListPagination


class ProductionAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProductionAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CategoryAPIList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = CandyShopAPIListPagination


class CategoryAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)


class CategoryAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
