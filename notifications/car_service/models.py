from django.db import models


class Parts(models.Model):
    title = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    installation_date = models.DateField(auto_now_add=False, auto_now=False)
    description = models.TextField(blank=True)
