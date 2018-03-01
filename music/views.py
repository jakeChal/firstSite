from django.http import HttpResponse
from .models import Album

# take user request and respond with something

def index(request):
    all_albums = Album.objects.all()
    html=''
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + album.albumTitle + '</a><br>'
    return HttpResponse(html)

def detail(request, album_id):
    return HttpResponse("<h2>Details for album id: " + str(album_id) + "</h2>")