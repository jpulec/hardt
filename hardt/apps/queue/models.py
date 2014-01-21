from django.db import models

from hardt.apps.tracks.models import Track

class OrderedTrack(models.Model):
    track = models.ForeignKey(Track)
    order = models.IntegerField()

    def __unicode__(self):
        return unicode(self.order) + ":" + unicode(self.track)
