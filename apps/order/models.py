"""Model File of Order"""
from django.db import models

from apps.asset.models import Asset


class Order(models.Model):
    """Model of Order"""

    class Meta:
        db_table = "ewallet_order"

    ORDER_TYPE = (
        (0, "BUY"),
        (1, "SELL")
    )

    order_id = models.AutoField(primary_key=True)
    type = models.PositiveIntegerField(choices=ORDER_TYPE, null=False, blank=False)
    quantity = models.DecimalField(max_digits=15, decimal_places=10, default=0.0, null=False, blank=False)
    asset_id = models.ForeignKey(Asset, on_delete=models.PROTECT, null=False, blank=False)
    date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Get name of order by default"""
        return self.type

    def asset(self):
        return self.asset_id
