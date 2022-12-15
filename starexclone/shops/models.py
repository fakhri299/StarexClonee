from django.db import models


class Shop(models.Model):

    CATEGORY_CHOICES=(
        ('Çin','Çin'),
        ('ABŞ','ABŞ'),
        ('Türkiyə','Türkiyə'),
    )


    shop_link=models.URLField(max_length=100,unique=True,blank=True)
    image=models.ImageField(upload_to="media/shop_photos/%Y/%m/%d/", null=True, blank=True)
    category=models.CharField(max_length=15,choices=CATEGORY_CHOICES,null=True,blank=True)

    class Meta:
        verbose_name_plural='Mağazalar'

    def __str__(self):
        return self.shop_link
