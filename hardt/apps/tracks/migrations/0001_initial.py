# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Artist'
        db.create_table(u'tracks_artist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'tracks', ['Artist'])

        # Adding model 'Album'
        db.create_table(u'tracks_album', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tracks.Artist'])),
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'tracks', ['Album'])

        # Adding model 'Track'
        db.create_table(u'tracks_track', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tracks.Artist'])),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tracks.Album'])),
            ('duration', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('path', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'tracks', ['Track'])


    def backwards(self, orm):
        # Deleting model 'Artist'
        db.delete_table(u'tracks_artist')

        # Deleting model 'Album'
        db.delete_table(u'tracks_album')

        # Deleting model 'Track'
        db.delete_table(u'tracks_track')


    models = {
        u'tracks.album': {
            'Meta': {'object_name': 'Album'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tracks.Artist']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'tracks.artist': {
            'Meta': {'object_name': 'Artist'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'tracks.track': {
            'Meta': {'object_name': 'Track'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tracks.Album']"}),
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tracks.Artist']"}),
            'duration': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['tracks']