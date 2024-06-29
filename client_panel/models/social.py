from django.db import models
from .base import BaseModel


class Social(BaseModel):
    name = models.CharField(max_length=20)
    link = models.CharField(max_length=100)





