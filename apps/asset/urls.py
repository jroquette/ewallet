"""Urls of Asset"""

from rest_framework import routers

from apps.asset.views import AssetViewSet


router = routers.DefaultRouter()
router.register(r'', AssetViewSet, basename='asset')

asset_urls = router.urls
