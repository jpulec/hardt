from django.contrib import admin

from hardt.apps.tracks.models import *

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Track)
