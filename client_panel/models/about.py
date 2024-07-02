from django.db import models
from .base import BaseModel


class About(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ism")
    profession = models.CharField(max_length=255, verbose_name="Kasbingiz")
    description = models.TextField(verbose_name="Ta'rif")
    image = models.ImageField(verbose_name="about/doctor")
    class Meta:
        verbose_name = "Ma'lumotlar"
        verbose_name_plural = "Ma'lumotlar"

    def __str__(self):
        return self.name
    
class Education(models.Model):
    text= models.TextField(verbose_name="Tahsil olgan joylarni kiriting")

    class Meta:
        verbose_name = "Taxsil"
        verbose_name_plural = "Tahsil olgan joylar"

    def __str__(self):
        return self.description
    
class EducationPro(models.Model):
    text = models.TextField(verbose_name="Malaka olgan joylarni kiriting")

    class Meta:
        verbose_name = "Malaka"
        verbose_name_plural = "Malaka olgan joylar"
    def __str__(self):
        return self.description


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


class AboutClinical(models.Model):
    text = models.TextField(verbose_name="Klinika haqida malumot kiriting")
    image = models.ImageField(upload_to="clinic/photo", verbose_name="Klinikaga oid rasm kiriting ")

    class Meta:
        verbose_name = "Klinika haqida malumot"
        verbose_name_plural = "Klinika haqida malumotlar"



