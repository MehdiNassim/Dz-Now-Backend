from django.shortcuts import get_list_or_404
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
