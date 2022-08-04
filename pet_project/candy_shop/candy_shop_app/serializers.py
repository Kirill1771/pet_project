from rest_framework import serializers

from .models import Production


class CandyShopSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Production
        fields = "__all__"
