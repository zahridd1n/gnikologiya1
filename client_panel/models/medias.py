from django.db import models
from .base import BaseModel


class Video(BaseModel):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    