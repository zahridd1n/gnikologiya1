from django.db import models
from .base import BaseModel
from ckeditor_uploader.fields import RichTextUploadingField

class About(BaseModel):
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    description = models.TextField()
    title = models.CharField(max_length=255)
    description1 = models.CharField(max_length=255)
    experiences_detail = RichTextUploadingField()

class Experience(BaseModel):
    about_info = models.ForeignKey(About, related_name='experiences', on_delete=models.CASCADE)

class Certificate(BaseModel):
    # Define your fields here
    pass
