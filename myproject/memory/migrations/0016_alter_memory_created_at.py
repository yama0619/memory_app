# Generated by Django 5.1.3 on 2024-12-01 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memory', '0015_alter_memory_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='created_at',
            field=models.DateField(),
        ),
    ]