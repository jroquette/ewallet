"""Views of Order"""

from rest_framework.viewsets import ModelViewSet

from apps.order.models import Order
from apps.order.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    """View of Order"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
