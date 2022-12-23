from django.db import models




class Country(models.Model):
    name=models.CharField(max_length=50,null=True)
    slug=models.SlugField(max_length=50,null=True)

    def __str__(self):
        return self.name



class CountryContact(models.Model):
    country=models.ForeignKey(Country,on_delete=models.DO_NOTHING,null=True)
    location=models.CharField(max_length=50,null=True)
    active_period=models.CharField(max_length=100,null=True)
    

    def __str__(self):
        return f'{self.location}'
    




class District(models.Model):
    name=models.CharField(max_length=50,null=True)
    slug=models.SlugField(max_length=50,null=True)


    def __str__(self):
        return self.name

class PointContact(models.Model):
    name=models.CharField(max_length=50,null=True)
    slug=models.SlugField(max_length=50,null=True)
    location=models.CharField(max_length=50,null=True)
    active_period=models.CharField(max_length=200,null=True)
    telephon=models.CharField(max_length=50,null=True,blank=True)
    district=models.ForeignKey(District,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.location}'



    

    