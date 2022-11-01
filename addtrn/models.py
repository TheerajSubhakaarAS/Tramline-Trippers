from turtle import distance
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class TrainDetails(models.Model):
    trno = models.IntegerField(null=True)
    trname = models.CharField(max_length =100)
    fromstn = models.CharField(max_length=100)
    tostn = models.CharField(max_length=100)
    Deptime = models.CharField(max_length=25)
    arrtime = models.CharField(max_length=25)
    fare = models.IntegerField(null = True)
    