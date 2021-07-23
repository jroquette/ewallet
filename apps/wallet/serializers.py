"""Serializer of Wallet"""

from rest_framework import serializers

from apps.wallet.models import Wallet, Investment
from apps.category.serializers import CategorySerializer


class WalletSerializer(serializers.ModelSerializer):
    """Serializer Class of Wallet"""
    category = CategorySerializer(read_only=True)

    class Meta:
        """Meta Class"""
        model = Wallet
        fields = "__all__"
        extra_kwargs = {'balance': {'read_only': True},
                        'category_id': {'write_only': True}}


class InvestmentSerializer(serializers.ModelSerializer):
    """Serializer Class of Investment"""

    class Meta:
        """Meta Class"""
        model = Investment
        fields = "__all__"
