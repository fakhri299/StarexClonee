# Generated by Django 4.1.4 on 2022-12-15 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created'], 'verbose_name_plural': 'Xəbərlər'},
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/news_photos/%Y/%m/%d/'),
        ),
    ]