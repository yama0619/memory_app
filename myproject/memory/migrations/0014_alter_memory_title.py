# Generated by Django 5.1.3 on 2024-12-01 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memory', '0013_alter_memory_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
