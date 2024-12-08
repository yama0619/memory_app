# Generated by Django 5.1.3 on 2024-12-01 05:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memory', '0011_alter_memory_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'mpeg'])]),
        ),
    ]
