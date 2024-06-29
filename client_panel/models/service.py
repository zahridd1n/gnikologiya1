from django.db import models
from .base import BaseModel


class Service(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField()







