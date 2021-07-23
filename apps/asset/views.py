"""Views of Asset"""

from rest_framework.viewsets import ModelViewSet

from apps.asset.models import Asset
from apps.asset.serializers import AssetSerializer


class AssetViewSet(ModelViewSet):
    """View of Asset"""
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
