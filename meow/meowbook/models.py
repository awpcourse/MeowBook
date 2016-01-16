from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class CatProfile(models.Model):
    name = models.TextField(max_length=30)
    description = models.TextField(max_length=500)
    avatar = models.ImageField(upload_to='images/', height_field=None, width_field=None)
    user = models.ForeignKey(User, related_name="cats")


class CatStatus(models.Model):
    text = models.TextField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)
    cat = models.ForeignKey(CatProfile, related_name="statuses")
    meowing_cats = models.ManyToManyField(CatProfile)


class CatPicture(models.Model):
    picture = models.ImageField(upload_to='images/', height_field=None, width_field=None)
    date_added = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=300)
    cat = models.ForeignKey(CatProfile, related_name="pictures")
    meowing_cats = models.ManyToManyField(CatProfile)


class PictureComment(models.Model):
    cat = models.ForeignKey(CatProfile, related_name="picture_comments")
    text = models.TextField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)


class StatusComment(models.Model):
    cat = models.ForeignKey(CatProfile, related_name="status_comments")
    text = models.TextField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):
    MASCULINE = 'M'
    FEMININE = 'F'
    sex_choices = (
        (MASCULINE, 'Masculine'),
        (FEMININE, 'Feminine'),
    )
    first_name = models.TextField(max_length=30)
    description = models.TextField(max_length=500)
    last_name = models.TextField(max_length=20)
    birth_date = models.DateTimeField()
    sex = models.CharField(max_length=2,
                           choices=sex_choices,
                           default=MASCULINE)
    user = models.OneToOneField(User, primary_key=True, related_name="profile")
    avatar = models.ImageField(upload_to='images/', height_field=None, width_field=None)


