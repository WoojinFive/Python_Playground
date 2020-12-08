# from django.template import loader
# from django.http import HttpResponse
# from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Album, Song


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


def favorite(request, id):
    album = get_object_or_404(Album, id=id)
    try:
        selected_song = album.song_set.get(id=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': 'You did not select a valid song',
        })
    else:
        # selected_song.is_favorite = not selected_song.is_favorite
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})
