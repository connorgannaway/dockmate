# Generated by Django 3.1 on 2021-02-12 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_auto_20210204_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.PositiveIntegerField(default=0, max_length=12),
        ),
    ]