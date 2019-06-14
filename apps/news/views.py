from django.shortcuts import get_list_or_404, render, get_object_or_404
from django.core.paginator import Paginator
from django.urls import reverse
from django.views import View
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article, Category, Source

# TODO: home view
@api_view(['GET'])
def home_view(request, language):
    return Response({}, status=status.HTTP_200_OK)


@api_view(['GET'])
def source_view(request, language, id, page=0):
    source = get_object_or_404(Source, is_enabled=True, id=id)
    data = get_list_or_404(Article, is_enabled=True, source=source.id, language=language)
    paginator = Paginator(data, per_page=10)

    articles = [{
        'id': x.title,
        'title': x.title,
        'content': x.content,
        'minutes_read': x.minutes_read,
        'cover_url': x.cover_url,
        'created_at': x.created_at,
        'category': {
            'id': x.category.id,
            'name': x.category.name,
            'background_url': x.category.background_url,
            'background_color': x.category.background_color,
            'text_color': x.category.text_color,
        },
        'url': reverse('ARTICLE_URL', kwargs={'language': language, 'slug': x.slug}),

    } for x in paginator.get_page(page)]

    return Response({
        'id': source.id,
        'name': source.name,
        'logo_url': source.logo_url,
        'background_color': source.background_color,
        'text_color': source.text_color,
        'website': source.website,
        'articles': articles,
    }, status=status.HTTP_200_OK)

# TODO: category view
@api_view(['GET'])
def category_view(request, language, id, page=0):
    return Response({}, status=status.HTTP_200_OK)


@api_view(['GET'])
def all_sources_view(request, language):
    data = get_list_or_404(Source, is_enabled=True, language=language)
    sources = [{
        'id': x.id,
        'name': x.name,
        'logo_url': x.logo_url,
        'background_color': x.background_color,
        'text_color': x.text_color,
        'website': x.website,
    } for x in data]
    return Response(sources, status=status.HTTP_200_OK)


@api_view(['GET'])
def all_categories_view(request, language):
    data = get_list_or_404(Category, is_enabled=True, language=language)
    categories = [{
        'id': x.id,
        'name': x.name,
        'background_url': x.background_url,
        'background_color': x.background_color,
        'text_color': x.text_color,
    } for x in data]
    return Response(categories, status=status.HTTP_200_OK)

# TODO: reading time view
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


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        data = get_object_or_404(Article, slug=kwargs['slug'], is_enabled=True, language=kwargs['language'])
        context = {'article': data}
        return render(request, 'article.html', context)
