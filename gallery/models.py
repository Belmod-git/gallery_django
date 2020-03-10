from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Painting(models.Model):
    name = models.CharField(max_length=20)
    money = models.IntegerField(default=0)
    image = models.ImageField(blank=True,null=True,upload_to='tu/')
    brief = models.CharField(max_length=200)
    info = models.CharField(max_length=500)
