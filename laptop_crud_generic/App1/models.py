from django.db import models

# Create your models here.

class Laptop(models.Model):
    lname = models.CharField(max_length=30)
    lcompany = models.CharField(max_length=30)
    lram = models.IntegerField()
    lrom = models.IntegerField()
    lprocessor = models.CharField(max_length=30)
    lweight = models.FloatField()

    def __str__(self):
        return f'Name={self.lname},company={self.lcompany}'