# Generated by Django 5.0.6 on 2024-06-30 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_panel', '0011_rename_image_article_image1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='video_link1',
            field=models.TextField(blank=True, null=True, verbose_name='Video havola'),
        ),
        migrations.AlterField(
            model_name='article',
            name='video_link2',
            field=models.TextField(blank=True, null=True, verbose_name='Video havola'),
        ),
        migrations.AlterField(
            model_name='article',
            name='video_link3',
            field=models.TextField(blank=True, null=True, verbose_name='Video havola'),
        ),
    ]
