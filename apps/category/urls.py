"""Urls of Category"""

from rest_framework import routers

from apps.category.views import CategoryViewSet


router = routers.DefaultRouter()
router.register(r'', CategoryViewSet)

category_urls = router.urls
