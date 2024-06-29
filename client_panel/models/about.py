from django.db import models
from .base import BaseModel
from ckeditor_uploader.fields import RichTextUploadingField


class About(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ism")
    profession = models.CharField(max_length=255, verbose_name="Kasbingiz")
    description = models.TextField(verbose_name="Ta'rif")
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    description1 = models.CharField(max_length=255, verbose_name="Ta'rif 1")

    class Meta:
        verbose_name = "Ma'lumotlar"
        verbose_name_plural = "Ma'lumotlar"

    def __str__(self):
        return self.name
    
class Experience(models.Model):
    text = models.TextField(verbose_name="Qayerlarda ishlaganingizni kiriting")
    class Meta:
        verbose_name = "Ishlagan joy"
        verbose_name_plural = "Ishlagan joylar"

    def __str__(self):
        return self.text
    

class Certificate(models.Model):
    image = models.ImageField(upload_to="certificate/images", verbose_name="Rasm")

    class Meta:
        verbose_name = "Sertifikat"
        verbose_name_plural = "Sertifikatlar"

    def __str__(self):
        return self.image

