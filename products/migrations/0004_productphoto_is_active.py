# Generated by Django 4.0.5 on 2022-06-26 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productphoto_is_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='productphoto',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
