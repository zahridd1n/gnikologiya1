from django.db import models
from .base import BaseModel
class Banner(BaseModel):
    image=models.ImageField(upload_to="banner/image")


class Logo(BaseModel):
    light=models.ImageField(upload_to="logo/image")
    dark=models.ImageField(upload_to="logo/image")

class Social(BaseModel):
    name = models.CharField(max_length=50)
    link = models.TextField()

class Address(models.Model):
    street = models.TextField()
    longitude = models.IntegerField()
    latitude = models.IntegerField()
    link = models.CharField(max_length=50)

class Phone(models.Model):
    phone = models.CharField(max_length=15)

class Result(BaseModel):
    name = models.CharField(max_length=200)
    descriptions = models.TextField()

class Comment(BaseModel):
    photo = models.ImageField(upload_to="comments/photo")
    descriptions = models.TextField()

class News(BaseModel):
    title = models.CharField(max_length=200)
    descriptions = models.TextField()
    number = models.IntegerField(blank=True,null=True)
