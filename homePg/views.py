from django.shortcuts import render
from song.models import Song
from band.models import Member
from band.models import Info

# Create your views here.

def home (request):
    songs = Song.objects
    members = Member.objects
    infos = Info.objects
    return render(request, 'home.html', {'songs':songs, 'members':members, 'infos':infos})
