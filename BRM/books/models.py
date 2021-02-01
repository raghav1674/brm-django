from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=30,blank=False,null=False)
    author = models.CharField(max_length=60,blank=False,null=False)
    price = models.FloatField(default=0)
    publisher = models.CharField(max_length=120)


    def __str__(self):
        return f'{self.title} - {self.author}'
