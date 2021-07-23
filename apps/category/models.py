"""Model File of Task"""
from django.db import models


class Category(models.Model):
    """Model of Category"""

    class Meta:
        db_table = "ewallet_category"

    category_id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255)
    abbreviation = models.CharField(max_length=8)
    category_parent = models.ForeignKey("Category", on_delete=models.PROTECT, related_name="parent",
                                        null=True, blank=True)

    def __str__(self):
        """Get name of category by default"""
        return self.name
