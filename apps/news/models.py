from django.db import models
from django.utils import timezone
from enum import Enum


class LanguageChoice(Enum):
    ar = "Arabic"
    fr = "French"
    CN = "Chinese"
    ES = "Spanish"


class LanguagesField(models.CharField):
    description = "The Language"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 2
        kwargs['choices'] = [(tag, tag.value) for tag in LanguageChoice]
        kwargs['default'] = 'fr'
        super().__init__(*args, **kwargs)


class Category(models.Model):
    """
    Category Model (exemple: Politique,Sport ...)
    """
    name = models.CharField(max_length=80)
    language = LanguagesField()
    background_url = models.URLField(default='https://images.pexels.com/photos/949587/pexels-photo-949587.jpeg')
    background_color = models.CharField(max_length=7, default='#000000')
    text_color = models.CharField(max_length=7, default='#ffffff')

    def __str__(self):
        return f"{self.name} | {self.language}"


class Source(models.Model):
    """
    Source Model (exemple: El Heddaf, Ennahar, Echourouk, Liberté, ...)
    """
    name = models.CharField(max_length=80)
    language = LanguagesField()
    logo_url = models.URLField(default='https://image.flaticon.com/icons/png/512/21/21601.png')
    background_color = models.CharField(max_length=7, default='#000000')
    text_color = models.CharField(max_length=7, default='#ffffff')

    def __str__(self):
        return f"{self.name} | {self.language}"


class Article(models.Model):
    """
    Contact us form messages
    """
    title = models.CharField(max_length=200)
    language = LanguagesField()
    content = models.TextField()
    minutes_read = models.IntegerField(default=5, max_length=15)
    cover_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now())
    source = models.ForeignKey(Source, related_name='source', on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, related_name='source', on_delete=models.SET_NULL)


    def __str__(self):
        return f"{self.title} | {self.language}"
