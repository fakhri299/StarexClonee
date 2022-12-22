from django.db import models




class Country(models.Model):
    name=models.CharField(max_length=50,null=True)
    slug=models.SlugField(max_length=50,null=True)

    def __str__(self):
        return self.name



class Contact(models.Model):
    country=models.ForeignKey(Country,on_delete=models.DO_NOTHING,null=True)
    location=models.CharField(max_length=50,null=True)
    first_time=models.CharField(max_length=50,null=True)
    last_time=models.CharField(max_length=50,null=True)
    first_day=models.CharField(max_length=50,null=True)
    last_day=models.CharField(max_length=50,null=True)

    def __str__(self):
        return f'{self.location}-{self.first_day}-{self.last_day}-{self.first_time}-{self.last_time}'
    



