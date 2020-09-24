from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=50)


class Boardgame(models.Model):
    name = models.CharField(max_length=50)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={ 'Boardgame_id': self.id })

class Reviews(models.Model):
    boardgame = models.ForeignKey(Boardgame, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



