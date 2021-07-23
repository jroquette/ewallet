"""Model File of Wallet"""
from django.db import models

from apps.category.models import Category
from apps.asset.models import Asset


class Wallet(models.Model):
    """Model of Wallet"""

    class Meta:
        db_table = "ewallet_wallet"

    wallet_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, db_column="category_id")
    name = models.TextField(max_length=255)
    describe = models.TextField(max_length=255, default=None, blank=True, null=True)
    balance = models.DecimalField(max_digits=15, decimal_places=10, default=0.0)
    investment = models.ManyToManyField(Asset, through="Investment")

    def __str__(self):
        """Get name of wallet by default"""
        return self.name

    def category(self):
        """Category identifier"""
        return self.category_id


class Investment(models.Model):
    """Model of Investment, this contabilize de assets in wallet"""

    class Meta:
        db_table = "ewallet_investment"

    investment_id = models.AutoField(primary_key=True)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="wallet")
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name="asset")
    quantity = models.DecimalField(max_digits=15, decimal_places=10, default=1.0)
