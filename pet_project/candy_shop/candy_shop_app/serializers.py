import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Production


class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Production
        fields = "__all__"
