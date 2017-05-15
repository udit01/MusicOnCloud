from django.conf.urls import url
from . import views

app_name = 'music'
#above is a namespace
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$' , views.DetailView.as_view(), name='detail'),

    # /music/album/add/
    url(r'album/add/$',views.AlbumCreate.as_view() , name='album-add'),

    # /music/album/2
    url(r'album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view() , name='album-update'),

    # /music/album/2/delete
    url(r'album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view() , name='album-delete'),

]

















# urlpatterns = [
#     # /music/
#     url(r'^$', views.index, name='index'),
#
#
#
#     # /music/<album.id>/##mapped with id of that album
#     url(r'^(?P<album_id>[0-9]+)/$' , views.detail, name='detail'),
#
#     # /music/<album.id>/favorite/
#     url(r'^(?P<album_id>[0-9]+)/favorite$', views.favorite, name='favorite'),
#
# ]
