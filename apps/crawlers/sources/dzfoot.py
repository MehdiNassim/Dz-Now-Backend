import requests
from bs4 import BeautifulSoup

url = "http://www.dzfoot.com/"
source_id = 13  # dzfoot
category_id = 8  # sport
language_id = 'fr'


def dzfoot_crawler():
    # get all new articles
    res = []
    r1 = requests.get(url)
    s1 = BeautifulSoup(r1.text, "html.parser")
    bloc = s1.find('ul', id="fil-actus-hp")
    # for each new article
    for link in bloc.find_all('a'):
        title = link.get_text()
        original_url = link.get('href')
        r2 = requests.get(link.get('href'))
        s2 = BeautifulSoup(r2.text, "html.parser")
        cover_url = s2.find('img', {'class': 'featured-img'}).get('src')
        content = s2.find('div', {'class': 'post-body'}).get_text()
        res.append({
            'title': title,
            'cover_url': cover_url,
            'language': language_id,
            'content': content,
            'source': source_id,
            'category': category_id,
            'original_url': original_url,
            'videos': [],
        })
    return res
