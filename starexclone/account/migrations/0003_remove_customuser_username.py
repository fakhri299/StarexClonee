# Generated by Django 4.1.4 on 2022-12-30 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_customuser_promocode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]
