from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', default='member_imageDefault')
    info = models.TextField()

class Info(models.Model):
    info = models.TextField()
