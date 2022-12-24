# Generated by Django 4.1.4 on 2022-12-24 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rates', '0002_alter_rate_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Methods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('slug', models.SlugField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tarif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_weight', models.FloatField(default=0)),
                ('last_weight', models.FloatField(default=0)),
                ('price', models.FloatField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='rate',
            name='type',
        ),
        migrations.DeleteModel(
            name='CargoMethod',
        ),
        migrations.DeleteModel(
            name='Rate',
        ),
        migrations.AddField(
            model_name='methods',
            name='tarif',
            field=models.ManyToManyField(to='rates.tarif'),
        ),
        migrations.AddField(
            model_name='country',
            name='cargo_type',
            field=models.ManyToManyField(to='rates.methods'),
        ),
    ]
