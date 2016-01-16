# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-16 10:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meowbook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='images/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='CatStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PictureComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatusComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='catpictures',
            name='cat',
        ),
        migrations.RemoveField(
            model_name='catpictures',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='catstatuses',
            name='cat',
        ),
        migrations.RemoveField(
            model_name='catstatuses',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='catWhoCommented',
        ),
        migrations.RemoveField(
            model_name='meowscomment',
            name='cat',
        ),
        migrations.RemoveField(
            model_name='meowscomment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='meowspictures',
            name='cat',
        ),
        migrations.RemoveField(
            model_name='meowspictures',
            name='user',
        ),
        migrations.RemoveField(
            model_name='meowsstatuses',
            name='cat',
        ),
        migrations.RemoveField(
            model_name='meowsstatuses',
            name='user',
        ),
        migrations.RemoveField(
            model_name='scratchcomment',
            name='cat',
        ),
        migrations.RemoveField(
            model_name='scratchcomment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='scratchpictures',
            name='cat',
        ),
        migrations.RemoveField(
            model_name='scratchpictures',
            name='user',
        ),
        migrations.RemoveField(
            model_name='scratchstatuses',
            name='cat',
        ),
        migrations.RemoveField(
            model_name='scratchstatuses',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='cats',
        ),
        migrations.AlterField(
            model_name='catprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cats', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='CatPictures',
        ),
        migrations.DeleteModel(
            name='CatStatuses',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='MeowsComment',
        ),
        migrations.DeleteModel(
            name='MeowsPictures',
        ),
        migrations.DeleteModel(
            name='MeowsStatuses',
        ),
        migrations.DeleteModel(
            name='ScratchComment',
        ),
        migrations.DeleteModel(
            name='ScratchPictures',
        ),
        migrations.DeleteModel(
            name='ScratchStatuses',
        ),
        migrations.AddField(
            model_name='statuscomment',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_comments', to='meowbook.CatProfile'),
        ),
        migrations.AddField(
            model_name='picturecomment',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='picture_comments', to='meowbook.CatProfile'),
        ),
        migrations.AddField(
            model_name='catstatus',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statuses', to='meowbook.CatProfile'),
        ),
        migrations.AddField(
            model_name='catstatus',
            name='meowing_cats',
            field=models.ManyToManyField(to='meowbook.CatProfile'),
        ),
        migrations.AddField(
            model_name='catpicture',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='meowbook.CatProfile'),
        ),
        migrations.AddField(
            model_name='catpicture',
            name='meowing_cats',
            field=models.ManyToManyField(to='meowbook.CatProfile'),
        ),
    ]