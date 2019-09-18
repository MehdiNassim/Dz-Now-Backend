import requests
from bs4 import BeautifulSoup
from .utils import get_video_ids

url = "http://www.elheddaf.com/videos/index?id=27553"
source_id = 3  # lexpression
category_id = 2  # politique
language_id = 'fr'


def elheddaf_crawler():
    res = []
    # get all new articles
    r1 = requests.get(url)
    print(get_video_ids(r1.text))
    return []
    s1 = BeautifulSoup(r1.text, "html.parser")
    bloc = s1.find('ul', {'class': 'list-slider'})
    # for each new article
    if not bloc:
        return []
    for li in bloc.find_all('li', {'class': 'video'}):
        link = li.find('a')
        img = link.find('img')
        title = img.get('alt')
        original_url = link.get('href')
        cover_url = img.get('data-src')
        r2 = requests.get(original_url)
        s2 = BeautifulSoup(r2.text, "html.parser")
        content = s2.find('div', {'class': 'module-article'}).get_text()
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
        print(item)
    return []
