from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.news import models
from .services import get_video_details
from .sources.dzfoot import dzfoot_crawler
from .sources.lexpression import lexpression_crawler
from .sources.lexpression_culture import lexpression_culture_crawler

ALL_CRAWLERS = [
    # dzfoot_crawler,
    lexpression_crawler,
    # lexpression_culture_crawler,
]


def create_video(url, title, cover, article_id):
    video = models.Video.objects.create(url=url, title=title, cover_url=cover, article_id=article_id)
    return video


def create_article(original_url, title, cover_url, content, language, source, category):
    article = models.Article.objects.create(
        title=title,
        cover_url=cover_url,
        language=language,
        content=content,
        original_url=original_url,
        source_id=source,
        category_id=category,
    )
    return article


def article_exists(original_url):
    return models.Article.objects.filter(original_url=original_url).exists()


@api_view(['POST', 'GET'])
def all_crawlers_view(request):
    for crawler in ALL_CRAWLERS:
        for article in crawler():
            if article and not article_exists(article['original_url']):
                ar = create_article(
                    article['original_url'],
                    article['title'],
                    article['cover_url'],
                    article['content'],
                    article['language'],
                    article['source'],
                    article['category'],
                )
                print(f"{ar.title} has been added")
                for video_id in article['videos']:
                    if video_id and isinstance(video_id, str):
                        try:
                            vid = get_video_details(video_id)
                            create_video(vid['url'], vid['title'], vid['cover'], ar.pk)
                            print(f"Video {vid['url']} has been added")
                        except Exception as e:
                            print('error', e)
            else:
                print(f"{article['title']} already existe")

    res = Response(status=status.HTTP_200_OK)
    res["Access-Control-Allow-Origin"] = "*"
    return res
