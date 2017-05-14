from django.conf.urls import url
from . import views

app_name = 'music'
#above is a namespace
urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),



    # /music/<album.id>/##mapped with id of that album
    url(r'^(?P<album_id>[0-9]+)/$' , views.detail, name='detail'),

    # /music/<album.id>/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite$', views.favorite, name='favorite'),

]
