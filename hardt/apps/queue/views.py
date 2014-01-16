from django.views.generic import TemplateView

class Queue(TemplateView):
    template_name = "queue/queue.html"
