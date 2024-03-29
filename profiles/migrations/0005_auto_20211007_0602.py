# Generated by Django 3.2.7 on 2021-10-07 03:02

from django.db import migrations, models
import django.utils.timezone
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20211006_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personal',
            name='certificates',
            field=models.FileField(blank=True, null=True, upload_to=profiles.models.user_documents_path),
        ),
        migrations.AlterField(
            model_name='personal',
            name='good_conduct',
            field=models.FileField(blank=True, null=True, upload_to=profiles.models.user_documents_path),
        ),
        migrations.AlterField(
            model_name='personal',
            name='id_back',
            field=models.ImageField(blank=True, null=True, upload_to=profiles.models.user_id_path),
        ),
        migrations.AlterField(
            model_name='personal',
            name='id_front',
            field=models.ImageField(blank=True, null=True, upload_to=profiles.models.user_id_path),
        ),
    ]
