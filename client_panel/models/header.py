from django.db import models
from .base import BaseModel
class Banner(BaseModel):
    image = models.ImageField(upload_to="banner/image", verbose_name="Banner rasmi")

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Bannerlar"


class Logo(BaseModel):
    light = models.ImageField(upload_to="logo/image", verbose_name="Logo (yorqin)")
    dark = models.ImageField(upload_to="logo/image", verbose_name="Logo (qorong'i)")

    class Meta:
        verbose_name = "Logo"
        verbose_name_plural = "Logolar"


class Social(BaseModel):
    name = models.CharField(max_length=50, verbose_name="Ijtimoiy tarmoq nomi")
    link = models.TextField(verbose_name="Ijtimoiy tarmoq havolasi")

    class Meta:
        verbose_name = "Ijtimoiy tarmoq"
        verbose_name_plural = "Ijtimoiy tarmoqlar"


class Address(models.Model):
    street = models.TextField(verbose_name="Ko'cha nomi")
    longitude = models.CharField(max_length=15,verbose_name="Uzunlik")
    latitude = models.CharField(max_length=15,verbose_name="Kenglik")
    link = models.CharField(max_length=50, verbose_name="Havola")

    class Meta:
        verbose_name = "Manzil"
        verbose_name_plural = "Manzillar"


class Phone(models.Model):
    phone = models.CharField(max_length=15, verbose_name="Telefon raqami")

    class Meta:
        verbose_name = "Telefon"
        verbose_name_plural = "Telefonlar"


class Result(BaseModel):
    name = models.CharField(max_length=200, verbose_name="Natija nomi")
    descriptions = models.TextField(verbose_name="Natija ta'rif")

    class Meta:
        verbose_name = "Natija"
        verbose_name_plural = "Natijalar"


class Comment(BaseModel):
    photo = models.ImageField(upload_to="comments/photo", verbose_name="Sharh rasmi")
    descriptions = models.TextField(verbose_name="Sharh ta'rif")

    class Meta:
        verbose_name = "Sharh"
        verbose_name_plural = "Sharhlar"


class News(BaseModel):
    title = models.CharField(max_length=200, verbose_name="Yangilik sarlavhasi")
    descriptions = models.TextField(verbose_name="Yangilik matni")
    number = models.IntegerField(blank=True, null=True, verbose_name="Raqami")

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"
