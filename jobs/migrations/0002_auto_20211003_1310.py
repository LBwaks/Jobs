# Generated by Django 3.2.7 on 2021-10-03 10:10

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(blank=True, default='job_images/jobs.jpg', null=True, upload_to='job_images/'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]