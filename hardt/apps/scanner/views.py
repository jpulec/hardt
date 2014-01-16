from django.views.generic import View
from django.conf import settings
from django.http import HttpResponse

import os
import logging
import inspect
from mutagen.easyid3 import EasyID3
from mutagen._id3util import ID3NoHeaderError

from hardt.apps.tracks.models import Track, Artist, Album

logger = logging.getLogger(__name__)

class Scan(View):

    def get(self, request, *args, **kwargs):
        for root, dirnames, filenames in os.walk(settings.MUSIC_DIR):
            for filename in filenames:
                if filename.lower().endswith('.mp3'):
                    try:
                        path = os.path.join(root, filename)
                        audio = EasyID3(path)
                        artist, created = Artist.objects.get_or_create(
                                name=audio['artist'][0] if 'artist' in audio else 'Unknown Artist')
                        album, created = Album.objects.get_or_create(
                                name=audio['album'][0] if 'album' in audio else 'Unknown Album',
                                artist=artist,
                                year=audio['year'][0] if 'year' in audio else None
                                )
                        track, created = Track.objects.get_or_create(
                                title=audio['title'][0] if 'title' in audio else 'Untitled Track',
                                artist=artist,
                                album=album,
                                path=path,
                                duration=audio['length'][0] if 'length' in audio else None
                                )
                    except ID3NoHeaderError as e:
                        logger.exception(e)
                    #track, created = Track.objects.get_or_create(name
                elif filename.lower().endswith('.ogg'):
                    pass
                elif filename.lower().endswith('.wav'):
                    pass
        return HttpResponse('')
                    #if filename.lower().endswith(x):
                    #    track, created = Track.objects.get_or_create(
                    #            name=

