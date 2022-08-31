from rest_framework import serializers
from .models import *


class ProductionSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(ProductionSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')

        if request and request.method == 'POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

    class Meta:
        model = Production
        fields = ('id', 'name_prod', 'category', 'price')
        extra_kwargs = {
            'id': {'read_only': True},
            'name_prod': {'required': True},
            'category': {'required': True},
            'price': {'required': True}
        }


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
        extra_kwargs = {
            'id': {'read_only': True},
            'name': {'required': True}
        }
