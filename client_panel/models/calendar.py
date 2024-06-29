from django.db import models
from .category import Category,SubCategory
from ckeditor_uploader.fields import RichTextUploadingField


class Weeks(models.Model):
    week_number = models.IntegerField(unique=True, verbose_name="Hafta raqami")
    week_title = models.CharField(max_length=50, verbose_name="Hafta nomi")
    image=models.ImageField(upload_to="calendar/images/",blank=True,null=True)
    class Meta:
        verbose_name = "Hafta"
        verbose_name_plural = "Haftalar"
    def __str__(self):
        return self.week_title


class WeekArticle(models.Model):
    title = models.CharField(max_length=300, verbose_name="Sarlavha")
    content = RichTextUploadingField(verbose_name="Maqola matni")
    image1 = models.ImageField(upload_to="weeks/image", blank=True, null=True, verbose_name="Rasm 1")
    image2 = models.ImageField(upload_to="weeks/image", blank=True, null=True, verbose_name="Rasm 2")
    video_link = models.TextField(verbose_name="Video havola",blank=True, null=True)
    week = models.ForeignKey(Weeks, on_delete=models.CASCADE, verbose_name="Hafta")


    class Meta:
        verbose_name = "Haftalik maqola"
        verbose_name_plural = "Haftalik maqolalar"
