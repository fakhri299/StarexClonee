# Generated by Django 4.1.4 on 2022-12-22 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contact_first_day_alter_contact_first_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='contact.country'),
        ),
    ]
