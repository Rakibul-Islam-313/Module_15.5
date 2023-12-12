from django.shortcuts import render
from album.models import Album
from musician.models import Musician
def Home(request):
    result = Album.objects.all()
    return render(request,'Home.html',{'result': result})