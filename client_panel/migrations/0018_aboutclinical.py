# Generated by Django 5.0.6 on 2024-07-01 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_panel', '0017_rename_description_education_text_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutClinical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Klinika haqida malumot kiriting')),
                ('image', models.ImageField(upload_to='clinic/photo', verbose_name='Klinikaga oid rasm kiriting ')),
            ],
            options={
                'verbose_name': 'Klinika haqida malumot',
                'verbose_name_plural': 'Klinika haqida malumotlar',
            },
        ),
    ]