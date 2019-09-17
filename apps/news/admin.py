from django.contrib import admin
from .models import Category, Source, Article, Video

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Source)
admin.site.register(Video)
