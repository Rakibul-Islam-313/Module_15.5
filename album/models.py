from django.db import models
from musician.models import Musician
# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=40)
    album_release_date = models.DateTimeField()
    rating = models.IntegerField()
    musicians =  models.ForeignKey(Musician, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.album_name