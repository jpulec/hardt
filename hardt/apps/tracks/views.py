from django.views.generic import TemplateView

from hardt.apps.tracks.models import Track

class Library(TemplateView):
    template_name = "tracks/library.html"

    def get_context_data(self, **kwargs):
        context = super(Library, self).get_context_data(**kwargs)
        context['tracks'] = Track.objects.all()[:100]
        return context
