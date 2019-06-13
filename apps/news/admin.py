from django.contrib import admin
from .models import Category, Source, Article

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Source)
