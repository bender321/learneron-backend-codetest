from django.db import models


class Actor(models.Model):

    name = models.CharField(max_length=25)
    date_of_birth = models.DateField(max_length=10)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return self.name



