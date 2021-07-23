"""Serializer of Order"""

from rest_framework import serializers

from apps.order.models import Order
from apps.asset.serializers import AssetSerializer


class OrderSerializer(serializers.ModelSerializer):
    """Serializer Class of Order"""
    value = serializers.SerializerMethodField()
    asset = AssetSerializer(read_only=True)

    def get_value(self, obj):
        """
        Get value of order

        :param obj: Instance of Order
        :return: value of order
        """
        value = obj.asset_id.price * obj.quantity
        return value

    class Meta:
        """Meta Class"""
        model = Order
        fields = "__all__"
        extra_kwargs = {'asset_id': {'write_only': True}}
