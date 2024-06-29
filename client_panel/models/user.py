# client_panel/models/user.py

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True,null=True, blank=True)
    file = models.FileField(upload_to='media/user_file',null=True, blank=True)
    confirm = models.BooleanField(default=False,null=True, blank=True) # True bo'lsa qabul qilingan bo'ladi

    def __str__(self):
        return self.username

