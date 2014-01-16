from django.db import models

class Artist(models.Model):
    name = models.TextField()

    def __unicode__(self):
        return unicode(self.name)

class Album(models.Model):
    name = models.TextField()
    artist = models.ForeignKey('Artist')
    year = models.IntegerField(null=True)

    def __unicode__(self):
        return unicode(self.name) + " (" + unicode(self.year) + ")"

class Track(models.Model):
    title = models.TextField()
    artist = models.ForeignKey('Artist')
    album = models.ForeignKey('Album')
    duration = models.IntegerField(null=True)  #do duration in secs
    path = models.TextField()

    def __unicode__(self):
        return unicode(self.title)
