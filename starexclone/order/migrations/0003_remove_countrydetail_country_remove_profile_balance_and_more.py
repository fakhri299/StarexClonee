# Generated by Django 4.1.4 on 2023-01-06 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_increasebalance_card_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countrydetail',
            name='country',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='foreign_adress',
        ),
        migrations.AddField(
            model_name='country',
            name='detail',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.countrydetail'),
        ),
    ]
