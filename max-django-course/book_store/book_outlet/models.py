from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
