# Generated by Django 2.2.2 on 2019-06-14 00:38

import apps.news.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('slug', models.SlugField(default='default', max_length=80, unique=True)),
                ('language', apps.news.models.LanguagesField(choices=[('ar', 'Arabic'), ('fr', 'French')], default=apps.news.models.LanguageChoice('fr'), max_length=2)),
                ('background_url', models.URLField(default='https://images.pexels.com/photos/949587/pexels-photo-949587.jpeg')),
                ('background_color', models.CharField(default='#000000', max_length=7)),
                ('text_color', models.CharField(default='#ffffff', max_length=7)),
                ('is_enabled', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('slug', models.SlugField(default='default', max_length=80, unique=True)),
                ('language', apps.news.models.LanguagesField(choices=[('ar', 'Arabic'), ('fr', 'French')], default=apps.news.models.LanguageChoice('fr'), max_length=2)),
                ('logo_url', models.URLField(default='https://image.flaticon.com/icons/png/512/21/21601.png')),
                ('background_color', models.CharField(default='#000000', max_length=7)),
                ('text_color', models.CharField(default='#ffffff', max_length=7)),
                ('is_enabled', models.BooleanField(default=True)),
                ('website', models.URLField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Sources',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(default='default', max_length=200, unique=True)),
                ('language', apps.news.models.LanguagesField(choices=[('ar', 'Arabic'), ('fr', 'French')], default=apps.news.models.LanguageChoice('fr'), max_length=2)),
                ('content', models.TextField()),
                ('minutes_read', models.IntegerField(default=5)),
                ('cover_url', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_enabled', models.BooleanField(default=True)),
                ('original_url', models.URLField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='source', to='news.Category')),
                ('source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='source', to='news.Source')),
            ],
            options={
                'verbose_name_plural': 'Articles',
            },
        ),
    ]
