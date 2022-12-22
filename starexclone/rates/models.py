from django.db import models










class Country(models.Model):
    name=models.CharField(max_length=50,null=True)
    slug=models.SlugField(max_length=50,null=True)


    def __str__(self):
        return self.slug


class CargoMethod(models.Model):
    name=models.CharField(max_length=50,null=True)
    slug=models.SlugField(max_length=50,null=True)
    country=models.ForeignKey(Country,on_delete=models.DO_NOTHING,null=True)

    def __str__(self):
        return f'{self.country} - {self.slug}'


class Rate(models.Model):
    type=models.ForeignKey(CargoMethod,on_delete=models.DO_NOTHING,null=True,related_name='rates')
    first_weight=models.FloatField(default=0)
    last_weight=models.FloatField(default=0)
    price=models.FloatField(default=0)


    def __str__(self):
        return f'{self.type} - {self.price}'






