from django.db import models
from .base import BaseModel

class Booking(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="To'liq ism")
    phone_number = models.CharField(max_length=15, verbose_name="Telefon raqami")
    status = models.BooleanField(default=False, verbose_name="Holat")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Sanasi")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Qabulga yozilganlar"
        verbose_name_plural = "Qabulga yozilganlar"

