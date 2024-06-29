from django.db import models
from .base import BaseModel

class About(BaseModel):
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    desciption = models.TextField()
    title = models.CharField(max_length=255)
    desciption1 = models.CharField()

class Experience(BaseModel):
    about = models.ForeignKey(About, related_name='experiences', on_delete=models.CASCADE)
    