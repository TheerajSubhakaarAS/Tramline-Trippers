from django.db import models

# Create your models here.

class BookingInfo(models.Model):
    user = models.CharField(max_length=100)
    pnr = models.IntegerField(null = True)
    trname = models.CharField(max_length=100)
    seats = models.IntegerField(default=1)
    status = models.CharField(max_length=100, default="confirmed")
    
    
    
    