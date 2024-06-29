from django.db import models
from .base import BaseModel
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Category(BaseModel):
    name = models.CharField(max_length=100)

class SubCategory(BaseModel):
    title = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class PodCategory(BaseModel):
    name = models.CharField(max_length=500)
    description = models.TextField()
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)




class Article(BaseModel):
    title = models.CharField(max_length=1000)
    content = models.TextField()
    image = models.ImageField(upload_to="contet/image")
    image1 = models.ImageField(upload_to="contet/image")
    image2 = models.ImageField(upload_to="contet/image")
    video_link = models.TextField()
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')