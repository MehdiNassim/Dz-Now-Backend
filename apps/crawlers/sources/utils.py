import re
from bs4 import BeautifulSoup


def get_video_ids(html_text):
    video_ids = re.findall('youtube.com\/embed\/([-\w]{11})', html_text)
    # video_ids = re.findall(
    #     '(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^"&?\/ ]{11})'
    #     , html_text)
    # for element in soup.find_all('embed'):
    #     src = element.get('src')
    #     if re.search('v\/([-\w]+)', src):
    #         videoids.append(re.search('v\/([-\w]+)', src).group(1))
    # for element in soup.find_all('iframe'):
    #     src = element.get('src')
    #     if re.search('youtube.com\/embed\/', src):
    #         videoids.append(re.search('embed\/([-\w]+)', src).group(1))
    # for element in soup.find_all('iframe'):
    #     src = element.get('src')
    #     if re.search('youtube.com\/embed\/', src):
    #         videoids.append(re.search('embed\/([-\w]+)', src).group(1))
    # for element in soup.find_all('a'):
    #     href = element.get('href')
    #     if href and re.search('youtube.com\/watch\?v=([-\w]+)', href):
    #         videoids.append(re.search('youtube.com\/watch\?v=([-\w]+)', href).group(1))
    #     if href and re.search('youtu\.be\/([-\w]+)', href):
    #         videoids.append(re.search('youtu\.be\/([-\w]+)', href).group(1))
    return video_ids
