from django.db import models

class Artist(models.Model):
    name = models.TextField()

class Album(models.Model):
    name = models.TextField()
    artist = models.ForeignKey('Artist')
    year = models.IntegerField()

class Track(models.Model):
    title = models.TextField()
    artist = models.ForeignKey('Artist')
    album = models.ForeignKey('Album')
    duration = models.IntegerField()  #do duration in secs
    path = models.TextField()
