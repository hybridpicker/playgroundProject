from django.db import models

# Create your models here.

class Member(models.Model):
    counter = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', default='member_imageDefault')
    info = models.TextField()
    def __str__(self):
        return '%s' % (self.name)
    class Meta:  # pylint: disable=too-few-public-methods
        '''
        Meta class for BandMember
        '''
        ordering = ('counter',)
        verbose_name = u'Band Member'
        verbose_name_plural = u'Band Members'

class Info(models.Model):
    info = models.TextField()
