import requests
from bs4 import BeautifulSoup
from .utils import get_video_ids

url = "https://www.lexpressiondz.com/culture"
source_id = 3  # lexpression
category_id = 5  # culture
language_id = 'fr'


def lexpression_culture_crawler():
    res = []
    # get all new articles
    r1 = requests.get(url)
    s1 = BeautifulSoup(r1.text, "html.parser")
    bloc = s1.find('ul', {'class': 'list-categories'})
    # for each new article
    if not bloc:
        return []
    for li in bloc.find_all('li'):
        link = li.find_all('a')[1]
        if not link:
            continue
        img = li.find('img')
        if not img:
            continue
        title = link.get_text()
        original_url = link.get('href')
        cover_url = img.get('data-src')
        r2 = requests.get(original_url)
        s2 = BeautifulSoup(r2.text, "html.parser")
        div = s2.find('div', {'class': 'module-article'})
        if not div:
            continue
        content = div.get_text()
        videos = get_video_ids(r2.text),
        item = {
            'title': title,
            'cover_url': cover_url,
            'language': language_id,
            'content': content,
            'source': source_id,
            'category': category_id,
            'original_url': original_url,
            'videos': videos,
        }
        res.append(item)
    return res
