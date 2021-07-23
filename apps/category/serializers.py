"""Serializer of Category"""

from rest_framework import serializers
from apps.category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Serializer Class of Category"""
    class Meta:
        """Meta Class"""
        model = Category
        fields = "__all__"
