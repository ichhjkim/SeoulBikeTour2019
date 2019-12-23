from django.db import models
from django.urls import reverse

class Spot(models.Model):
    name = models.TextField()
    rating = models.FloatField()
    explain = models.TextField()
    mapy = models.FloatField() #latitude
    mapx = models.FloatField() #longitude
    imagelink = models.TextField()
    address = models.TextField()
    category = models.TextField()

class Bicycle(models.Model):
    idnum = models.IntegerField()
    stationname = models.TextField()
    address = models.TextField()
    mapy = models.FloatField() #latitude
    mapx = models.FloatField() #longitude
    parkingnum = models.IntegerField()
    possiblebikenum = models.IntegerField()
