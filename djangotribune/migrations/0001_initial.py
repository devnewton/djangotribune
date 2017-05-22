# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-14 22:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('slug', models.SlugField(max_length=75, unique=True, verbose_name='slug')),
                ('title', models.CharField(max_length=55, verbose_name='title')),
            ],
            options={
                'verbose_name': 'channel',
                'verbose_name_plural': 'channels',
            },
        ),
        migrations.CreateModel(
            name='FilterEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.CharField(choices=[('user_agent', 'User Agent'), ('owner__username', 'Username'), ('raw', 'Raw message')], max_length=30, verbose_name='target')),
                ('kind', models.CharField(choices=[('contains', 'Case-sensitive containment test'), ('icontains', 'Case-insensitive containment test'), ('exact', 'Case-sensitive exact match'), ('iexact', 'Case-insensitive exact match'), ('startswith', 'Case-sensitive starts-with'), ('endswith', 'Case-sensitive ends-with')], max_length=30, verbose_name='kind')),
                ('value', models.CharField(max_length=255, verbose_name='value')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user message filter',
                'verbose_name_plural': 'user message filters',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(verbose_name='created date')),
                ('clock', models.TimeField(blank=True, verbose_name='clock')),
                ('user_agent', models.CharField(max_length=150, verbose_name='User Agent')),
                ('ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP adress')),
                ('raw', models.TextField(verbose_name='raw')),
                ('web_render', models.TextField(verbose_name='html')),
                ('remote_render', models.TextField(verbose_name='xml')),
                ('channel', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangotribune.Channel', verbose_name='channel')),
                ('owner', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'messages',
            },
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, verbose_name='created date')),
                ('url', models.TextField(verbose_name='url')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangotribune.Message')),
                ('owner', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'url',
                'verbose_name_plural': 'urls',
            },
        ),
        migrations.CreateModel(
            name='UserPreferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('refresh_time', models.IntegerField(default=5000, verbose_name='refresh time')),
                ('refresh_actived', models.BooleanField(default=True, verbose_name='refresh actived')),
                ('smileys_host_url', models.CharField(max_length=150, verbose_name='smileys host url')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user preference',
                'verbose_name_plural': 'user preferences',
            },
        ),
    ]
