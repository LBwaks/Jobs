# Generated by Django 3.2.7 on 2021-10-07 18:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0003_auto_20211007_0623'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='other_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
