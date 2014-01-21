from django.views.generic import TemplateView
from django.views.generic.edit import ProcessFormView
from django.db.models import Max

from hardt.apps.queue.models import OrderedTrack
from hardt.apps.tracks.models import Track

class Queue(TemplateView):
    template_name = "queue/queue.html"

    def post(self, request, *args, **kwargs):
        if "trackId" in self.request.POST:
            order = OrderedTrack.objects.aggregate(Max('order'))['order__max']
            if not order:
                order = 0
            track=Track.objects.get(id=self.request.POST['trackId'])
            ordered_track = OrderedTrack.objects.create(track=track,
                                                 order=order + 1)
        return super(Queue, self).get(request, *args, **kwargs)
