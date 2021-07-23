"""Serializer of Asset"""

from rest_framework import serializers

from apps.asset.models import Asset
from apps.category.serializers import CategorySerializer


class AssetSerializer(serializers.ModelSerializer):
    """Serializer Class of Asset"""
    category = CategorySerializer(read_only=True)

    class Meta:
        """Meta Class"""
        model = Asset
        fields = "__all__"
        extra_kwargs = {'category_id': {'write_only': True}}
