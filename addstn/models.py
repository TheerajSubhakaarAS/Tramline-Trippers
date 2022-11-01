from django.db import models

# Create your models here.
class Stationdetails(models.Model):
    trnamee = models.CharField(max_length =100)
    stn = models.CharField(max_length=100)
    time = models.CharField(max_length=25)
    fare = models.IntegerField(null = True)
