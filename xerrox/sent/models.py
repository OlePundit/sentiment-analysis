from django.db import models
from datetime import datetime
# Create your models here.

class Query(models.Model):
    tweets = models.CharField(max_length=200)
    users = models.CharField(max_length=200)
    urls = models.CharField(max_length=200)

class Results(models.Model):
    query = models.CharField(max_length=200)
  
