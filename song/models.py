from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', default='imageDefault')
    audio = models.FileField(upload_to='audio/', default='audioDefault')
