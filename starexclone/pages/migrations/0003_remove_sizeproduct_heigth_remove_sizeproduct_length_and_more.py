# Generated by Django 4.1.4 on 2022-12-13 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_sizeproduct_shipping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sizeproduct',
            name='heigth',
        ),
        migrations.RemoveField(
            model_name='sizeproduct',
            name='length',
        ),
        migrations.RemoveField(
            model_name='sizeproduct',
            name='width',
        ),
    ]
