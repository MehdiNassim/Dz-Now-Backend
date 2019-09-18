from django.urls import path
from . import views

urlpatterns = [
    path('crawlers/', views.all_crawlers_view),
]
