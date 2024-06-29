from django.db import models
from .base import BaseModel


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

class SubCategory(models.Model):
    title = models.CharField(max_length=500, verbose_name="Subkategoriya nomi")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoriya")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Subkategoriya"
        verbose_name_plural = "Subkategoriyalar"


class PodCategory(models.Model):
    name = models.CharField(max_length=500, verbose_name="Podkategoriya nomi")
    description = models.TextField(verbose_name="Podkategoriya tavsifi")
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name="Subkategoriya")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Podkategoriya"
        verbose_name_plural = "Podkategoriyalar"

class Article(models.Model):
    title = models.CharField(max_length=1000, verbose_name="Maqola sarlavhasi")
    content = models.TextField(verbose_name="Maqola matni")
    image = models.ImageField(upload_to="content/images/", blank=True, null=True, verbose_name="Rasm")
    video_link = models.TextField(blank=True, null=True, verbose_name="Video havola")
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name="Subkategoriya")
    pod_category = models.ForeignKey(PodCategory, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Podkategoriya")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Maqola"
        verbose_name_plural = "Maqolalar"
