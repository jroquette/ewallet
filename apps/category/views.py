"""Views of Category"""

from rest_framework.viewsets import ModelViewSet

from apps.category.models import Category
from apps.category.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    """View of Category"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
