# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
# Django automatically assigns unique ID numbers or a primary or unique key

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    #I dont know how to upload pics yet so we will take urls from internet
    def get_absolute_url(self):
        return reverse('music:detail',kwargs={ 'pk' : self.pk})
    def __str__(self):
        return self.album_title + ' - ' + self.artist

class Song(models.Model):
    #needs to be a part of album
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    #is a variable inside song class and its key is the 'album's' primary key
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    # is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return  self.song_title

