from django.views.generic import TemplateView

class Playlists(TemplateView):
    template_name = "playlists/playlists.html"
