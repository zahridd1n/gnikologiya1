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


class Certificate(BaseModel):
    image = models.ImageField(upload_to="sertificate/image")
2
