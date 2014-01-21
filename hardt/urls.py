from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from hardt.apps.nowplaying.views import Home, System
from hardt.apps.tracks.views import Library
from hardt.apps.scanner.views import Scan
from hardt.apps.playlists.views import Playlists
from hardt.apps.queue.views import Queue
from hardt.apps.search.views import Search

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name="home"),
    url(r'^system/$', System.as_view(), name="system"),
    url(r'^playlists/$', Playlists.as_view(), name="playlists"),
    url(r'^library/$', Library.as_view(), name="library"),
    url(r'^search/$', Search.as_view(), name="search"),
    url(r'^queue/$', Queue.as_view(), name="queue"),
    url(r'^scan/$', Scan.as_view(), name="scan"),
    url(r'^admin/', include(admin.site.urls)),
)
