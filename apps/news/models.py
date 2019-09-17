from django.db import models
from django.utils.timezone import now
from enum import Enum
from unidecode import unidecode
from django.template.defaultfilters import slugify
from .utils import minutes_read_calculator


class LanguageChoice(Enum):
    Arabic = "ar"
    French = "fr"


class LanguagesField(models.CharField):
    description = "The Language"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 2
        kwargs['choices'] = [(tag.value, tag.name) for tag in LanguageChoice]
        kwargs['default'] = LanguageChoice.French
        super().__init__(*args, **kwargs)


class Category(models.Model):
    """
    Category Model (exemple: Politique,Sport ...)
    """
    name = models.CharField(max_length=80)
    slug = models.SlugField(unique=True, max_length=80, default='default')
    language = LanguagesField()
    background_url = models.URLField(default='https://images.pexels.com/photos/949587/pexels-photo-949587.jpeg')
    background_color = models.CharField(max_length=7, default='#000000')
    text_color = models.CharField(max_length=7, default='#ffffff')
    is_enabled = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # newly created object
        if not self.id:
            if not self.slug or self.slug == 'default':
                self.slug = slugify(self.name)
            else:
                self.slug = slugify(self.slug)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} | {self.language}"

    class Meta:
        verbose_name_plural = "Categories"


class Source(models.Model):
    """
    Source Model (exemple: El Heddaf, Ennahar, Echourouk, Liberté, ...)
    """
    name = models.CharField(max_length=80)
    slug = models.SlugField(unique=True, max_length=80, default='default')
    language = LanguagesField()
    logo_url = models.URLField(default='https://image.flaticon.com/icons/png/512/21/21601.png')
    background_color = models.CharField(max_length=7, default='#000000')
    text_color = models.CharField(max_length=7, default='#ffffff')
    is_enabled = models.BooleanField(default=True)
    website = models.URLField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} | {self.language}"

    class Meta:
        verbose_name_plural = "Sources"

    def save(self, *args, **kwargs):
        # newly created object
        if not self.id and not self.slug:
            if not self.slug or self.slug == 'default':
                self.slug = slugify(self.name)
            else:
                self.slug = slugify(self.slug)
        super(Source, self).save(*args, **kwargs)


class Article(models.Model):
    """
    Article Model
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200, default='default')
    language = LanguagesField()
    content = models.TextField()
    minutes_read = models.IntegerField(default=0)
    cover_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(default=now)
    source = models.ForeignKey(Source, null=True, blank=True, related_name='articles', on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, blank=True, related_name='articles', on_delete=models.SET_NULL)
    is_enabled = models.BooleanField(default=True)
    original_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} | {self.language}"

    class Meta:
        verbose_name_plural = "Articles"
        get_latest_by = 'created_at'
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        # TODO: Add Test source and category same language
        # only newly created object
        if not self.id:
            if not self.slug or self.slug == 'default':
                self.slug = slugify(unidecode(self.title))
            else:
                self.slug = slugify(unidecode(self.slug))
            if self.minutes_read == 0:
                self.minutes_read = minutes_read_calculator(self.content)
        super(Article, self).save(*args, **kwargs)


class Video(models.Model):
    url = models.URLField(unique=True)
    is_enabled = models.BooleanField(default=True)
    title = models.CharField(max_length=255)
    cover_url = models.URLField(null=True, blank=True)
    article = models.ForeignKey(Article, null=True, blank=True, related_name='videos', on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.title} | {self.url}"
