from django.db import models
from django.conf import settings

# Create your models here.


class SizeProduct(models.Model):

    COUNTRY_CHOICES=(
        ('çin','ÇİN'),
        ('abş','ABŞ'),
        ('türkiyə','TÜRKİYƏ')
    )


    SHIPPING_CHOCIES=(
        ('adress','Adresə çatdırılma'),
        ('filial','Filiala çatdırlıma')
    )


    
    country=models.CharField(max_length=50,default='TÜRKİYƏ',choices=COUNTRY_CHOICES)
    shipping=models.CharField(max_length=50,default='Adresə çatdırılma',choices=SHIPPING_CHOCIES)
    weight=models.FloatField()
    price=models.FloatField(default=0)
    


    # @property
    # def get_price(self):
    #     if self.country == 'TÜRKİYƏ':
    #         return self.weight * 4
        
    #     elif self.country == 'ÇİN':
    #         return self.weight * 8

    #     elif self.country == 'ABŞ':
    #         return self.weight * 9
    
    def __str__(self) :
        return str(self.id)


    
    