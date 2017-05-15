from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from  .models import Album
#we are going to make generic views..

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'albums'
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')



















# # # -*- coding: utf-8 -*-
# # from __future__ import unicode_literals
# #
# # from django.shortcuts import render
# #
# # # Create your views here.
# # from django.http import HttpResponse
# from .models import Album,Song ###WHY do we have .models here why . ?
# #from django.template import loader
# from django.shortcuts import render, get_object_or_404
# # from django.http import Http404
#
#
#
# def index(request):
#     #variables to store the result of database call
#     all_albums = Album.objects.all()
#     #template = loader.get_template('music/index.html')
#
#     context = {
#         'all_albums': all_albums,
#     }
#
#     #return HttpResponse(template.render(context, request))
#     return render(request,'music/index.html',context)
# #render automatically converts it into http response
# def detail(request, album_id):
#     # return HttpResponse("<h3>Details for Album id: " + str(album_id) + "</h3>")
#     # try:
#     #     album = Album.objects.get(pk=album_id)
#     # except Album.DoesNotExist:
#     #     raise Http404("Sorry this album does not exist")
#
#     album = get_object_or_404(Album, pk=album_id)
#     #one liner for above 4 lines automatic
#     return render(request,'music/detail.html', {'album':album})
#
# def favorite(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     try:
#         selected_song = album.song_set.get(pk=request.POST['song'])
#     except(KeyError,Song.DoesNotExist):
#         return  render(request, 'music/detail.html', {
#             'album':album,
#             'error_message':"You did not select a valid song."
#         })
#
#     else:
#         selected_song.is_favorite = True
#         selected_song.save()
#         return render(request, 'music/detail.html', {'album': album})

