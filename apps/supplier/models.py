from django.db import models

# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    products_supplied = models.TextField(null=True, blank=True)
    lead_time = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name