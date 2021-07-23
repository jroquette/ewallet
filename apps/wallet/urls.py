"""Urls of Wallet"""

from rest_framework import routers

from apps.wallet.views import WalletViewSet, InvestmentViewSet


router = routers.DefaultRouter()
router.register(r'', WalletViewSet, basename='wallet')
router.register(r'', InvestmentViewSet, basename='investment')

wallet_urls = router.urls
