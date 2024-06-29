from django.db import models
from .base import BaseModel
class Banner(BaseModel):
    image=models.ImageField(upload_to="banner/image")




