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
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from apps.news import views

urlpatterns = [
    # admin
    url(r'^jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    # APIs
    # path('api/v0/now_playing/<int:station_id>/', radio_views.NowPlaying.as_view(), name='NOW_PLAYING_HOOK'),
    # path('api/v0/dedication/', DedicationUploadAPIView.as_view(), name='DEDICATION_UPLOAD_API'),
    # path('api/v0/', radio_views.PlaylistsDetailsAPIView.as_view(), name='PLAYLISTS_API'),
    # WEB
    path('', TemplateView.as_view(template_name='hello_world.html')),
    # STATIC
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]

# for serving media in dev mode
if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
