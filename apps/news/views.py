from django.shortcuts import get_list_or_404, render, get_object_or_404
from django.views import View
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article, Category, Source


@api_view(['GET'])
def home_view(request, language):
    return Response({}, status=status.HTTP_200_OK)


@api_view(['GET'])
def source_view(request, language, id, page=0):
    return Response({}, status=status.HTTP_200_OK)


@api_view(['GET'])
def category_view(request, language, id, page=0):
    return Response({}, status=status.HTTP_200_OK)


@api_view(['GET'])
def all_sources_view(request, language):
    # sources = Stemmer.objects.filter(is_enabled=True, )
    return Response({}, status=status.HTTP_200_OK)


@api_view(['GET'])
def all_categories_view(request, language):
    categories = get_list_or_404(Category, is_enabled=True, language=language)
    return Response(categories, status=status.HTTP_200_OK)


@api_view(['GET'])
def reading_time_view(request, language, minutes, page=0):
    return Response({}, status=status.HTTP_200_OK)


class SourcesView(View):
    def get(self, request, *args, **kwargs):
        data = get_list_or_404(Source, is_enabled=True)
        context = {'sources': data}
        return render(request, 'sources.html', context)


class SourceView(View):
    def get(self, request, *args, **kwargs):
        data = get_object_or_404(Source, slug=kwargs['slug'], is_enabled=True)
        context = {'source': data}
        return render(request, 'source.html', context)


class CategoriesView(View):
    def get(self, request, *args, **kwargs):
        data = get_list_or_404(Category, is_enabled=True)
        context = {'categories': data}
        return render(request, 'categories.html', context)


class CategoryView(View):
    def get(self, request, *args, **kwargs):
        data = get_object_or_404(Category, slug=kwargs['slug'], is_enabled=True)
        context = {'category': data}
        return render(request, 'category.html', context)
