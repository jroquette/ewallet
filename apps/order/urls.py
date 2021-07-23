"""Urls of Order"""

from rest_framework import routers

from apps.order.views import OrderViewSet


router = routers.DefaultRouter()
router.register(r'', OrderViewSet, basename='order')

order_urls = router.urls
