# Generated by Django 4.1.4 on 2022-12-23 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_sizeproduct_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalculateShipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50, null=True)),
                ('near_filial', models.CharField(blank=True, max_length=50, null=True)),
                ('far_filial', models.CharField(blank=True, max_length=50, null=True)),
                ('input_weight', models.FloatField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='SizeProduct',
        ),
    ]
