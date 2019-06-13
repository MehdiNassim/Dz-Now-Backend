from django.db import models
from django.utils.timezone import now
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
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} | {self.language}"

    class Meta:
        verbose_name_plural = "Categories"


class Source(models.Model):
    """
    Source Model (exemple: El Heddaf, Ennahar, Echourouk, Liberté, ...)
    """
    name = models.CharField(max_length=80)
    language = LanguagesField()
    logo_url = models.URLField(default='https://image.flaticon.com/icons/png/512/21/21601.png')
    background_color = models.CharField(max_length=7, default='#000000')
    text_color = models.CharField(max_length=7, default='#ffffff')
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} | {self.language}"

    class Meta:
        verbose_name_plural = "Sources"


class Article(models.Model):
    """
    Article Model
    """
    title = models.CharField(max_length=200)
    language = LanguagesField()
    content = models.TextField()
    minutes_read = models.IntegerField(default=5)
    cover_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(default=now)
    source = models.ForeignKey(Source, null=True, blank=True, related_name='source', on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, blank=True, related_name='source', on_delete=models.SET_NULL)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} | {self.language}"

    class Meta:
        verbose_name_plural = "Articles"
