# Generated by Django 2.2.5 on 2019-09-22 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20190922_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image_logo',
            field=models.ImageField(blank=True, upload_to='companies'),
        ),
    ]
