from django.shortcuts import render
# from django.template import loader
from django.http import HttpResponse
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    # template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'music/index.html', context)


def detail(request, id):
    return HttpResponse('<h2>Details for Album id: ' + str(id) + '</h2>')
