from django.db import models

# Create your models here.
class Search(models.Model):
    genre = models.CharField(max_length=100)
    city = models.CharField(max_length=100)