from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    production_capacity = models.IntegerField(null=True, blank=True)
    production_schedule = models.TextField(null=True, blank=True)
    products_produced = models.TextField(null=True, blank=True)
    quality_control_procedures = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name