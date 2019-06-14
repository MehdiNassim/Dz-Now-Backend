"""DZ_NOW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, register_converter
from django.views.generic import TemplateView
from django.conf import settings
from apps.news import views, converters

# /api/v0
#   /<language_code>/all
#   /<language_code>/source/<source_id>/<page_number>
#   /<language_code>/category/<category_id>/<page_number>
#   /<language_code>/categories
#   /<language_code>/sources
#   /<language_code>/reading_time/<minutes>/<page_number>

# TODO: remove language_code from source,category (it is already associated to the category)

register_converter(converters.LanguageConverter, 'language_code')

urlpatterns = [
    # admin
    url(r'^jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    # APIs
    path('api/v0/<language_code:language>/all/', views.home_view, name='HOME_API'),
    # SOURCE
    path('api/v0/<language_code:language>/source/<int:id>/', views.source_view, name='SOURCE_API'),
    path('api/v0/<language_code:language>/source/<int:id>/<int:page>/', views.source_view, name='SOURCE_API_PAGING'),
    # CATEGORY
    path('api/v0/<language_code:language>/category/<int:id>/', views.category_view, name='CATEGORY_API'),
    path('api/v0/<language_code:language>/category/<int:id>/<int:page>/', views.category_view,
         name='CATEGORY_API_PAGING'),
    # CATEGORIES
    path('api/v0/<language_code:language>/categories/', views.all_categories_view, name='CATEGORIES_API'),
    # SOURCES
    path('api/v0/<language_code:language>/sources/', views.all_sources_view, name='SOURCES_API'),
    # READING TIME FILTER
    path('api/v0/<language_code:language>/reading_time/<int:minutes>/', views.reading_time_view,
         name='READING_TIME_API'),
    path('api/v0/<language_code:language>/reading_time/<int:minutes>/<int:page>/', views.reading_time_view,
         name='READING_TIME_API_PAGING'),
    # WEB
    path('<language_code:language>/article/<slug:slug>/', views.ArticleView.as_view(), name='ARTICLE_URL'),
    path('source/<slug:slug>/', views.SourceView.as_view(), name='SOURCE_URL'),
    path('sources/', views.SourcesView.as_view(), name='SOURCES_URL'),
    path('category/<slug:slug>/', views.CategoryView.as_view(), name='CATEGORY_URL'),
    path('categories/', views.CategoriesView.as_view(), name='CATEGORIES_URL'),
    path('', TemplateView.as_view(template_name='home.html'), name='HOME_URL'),
    # STATIC
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]

# for serving media in dev mode
if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
