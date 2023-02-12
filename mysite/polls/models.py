from django.db import models
from django import forms

# Create your models here.
class MyModel(models.Model):
    field1 = models.CharField(max_length=50)
    field2 = models.IntegerField()

class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
