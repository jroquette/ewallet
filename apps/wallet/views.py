"""Views of Wallet"""

from rest_framework.viewsets import ModelViewSet

from apps.wallet.models import Wallet, Investment
from apps.wallet.serializers import WalletSerializer, InvestmentSerializer


class WalletViewSet(ModelViewSet):
    """View of Wallet"""
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class InvestmentViewSet(ModelViewSet):
    """View of Investment"""
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
