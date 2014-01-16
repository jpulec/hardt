from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = "nowplaying/home.html"

class System(TemplateView):
    template_name = "nowplaying/system.html"
