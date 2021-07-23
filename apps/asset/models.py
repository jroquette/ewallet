"""Model File of Asset"""
from django.db import models

from apps.category.models import Category


class Asset(models.Model):
    """Model of Asset"""

    class Meta:
        db_table = "ewallet_asset"

    asset_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, db_column="category_id")
    name = models.TextField(max_length=255)
    abbreviation = models.CharField(max_length=8, unique=True)
    price = models.DecimalField(max_digits=15, decimal_places=10, default=0.0)

    def __str__(self):
        """Get name of asset by default"""
        return self.name

    def category(self):
        """Category identifier"""
        return self.category_id
