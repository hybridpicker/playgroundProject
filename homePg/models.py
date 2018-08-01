from django.db import models

# Create your models here.

photo = models.ImageField(upload_to="gallery")

class Song(models.Model):
    title = models.CharField(max_length=100)
    songfile = models.FileField()
    isPlaying = False
