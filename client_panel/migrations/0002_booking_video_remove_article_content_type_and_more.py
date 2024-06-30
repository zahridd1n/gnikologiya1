# Generated by Django 5.0.6 on 2024-06-29 20:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_panel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('status', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='article',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='article',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='article',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='article',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='article',
            name='object_id',
        ),
        migrations.RemoveField(
            model_name='article',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='article',
            name='pod_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client_panel.podcategory'),
        ),
        migrations.AddField(
            model_name='article',
            name='sub_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='client_panel.subcategory'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='content/images/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='video_link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Weeks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_number', models.IntegerField(unique=True)),
                ('week_title', models.CharField(max_length=50)),
                ('week_description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_panel.category')),
            ],
        ),
        migrations.CreateModel(
            name='WeekArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('image1', models.ImageField(blank=True, null=True, upload_to='weeks/image')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='weeks/image')),
                ('video_link', models.TextField()),
                ('week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_panel.weeks')),
            ],
        ),
    ]