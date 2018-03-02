from django.contrib import admin
from .models import Album, Song

# E.g. delete users/ posts whateva

admin.site.register(Album)
admin.site.register(Song)