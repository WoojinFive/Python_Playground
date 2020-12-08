# from django.template import loader
# from django.http import HttpResponse
# from django.http import Http404
from django.shortcuts import render, get_object_or_404
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
    # try:
    #     album = Album.objects.get(id=id)
    # except Album.DoesNotExist:
    #     raise Http404("Album does not exist")
    album = get_object_or_404(Album, id=id)
    return render(request, 'music/detail.html', {'album': album})
