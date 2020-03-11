from django.db import models

class Unit(models.Model):
    unit_title = models.CharField(max_length=10)
    unit_description = models.CharField(max_length=30)

class OrderPre (models.Model):
    kind_board = models.CharField(max_length=10)
    thikness  = models.FloatField()
    lenght = models.IntegerField()
    widht = models.IntegerField()
    quantity = models.IntegerField()










# Create your models here.
