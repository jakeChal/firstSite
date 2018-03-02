from django.db import models

# Blueprint of your DB

class Album(models.Model):
    artist = models.CharField(max_length=100)
    albumTitle = models.CharField(max_length=150)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=100)

    def __str__(self):
        return self.albumTitle + ' - ' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=200)

    def __str__(self):
        return self.song_title