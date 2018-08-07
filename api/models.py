from django.contrib.auth.models import User
from django.db import models


class Member(models.Model):
    """
    Any user info that's not in the Django User obj
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='member')
    avatar = models.ImageField()
    display_name = models.CharField()


class Artist(models.Model):
    members = models.ManyToManyField(Member, related_name='artists')
    name = models.CharField()


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='song')
    name = models.CharField()
