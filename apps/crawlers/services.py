import requests
import json

youtubeAPI = 'https://www.googleapis.com/youtube/v3/videos'
API_KEY = 'AIzaSyB-lgOXvFyr66HGb5QLQB23DSUeYgVHlJ4'


def get_video_details(video_id):
    res = requests.get(youtubeAPI, params={
        'key': API_KEY,
        'id': video_id,
        'part': 'id,snippet',
    })
    data = json.loads(res.text)
    data = data['items'][0]['snippet']
    return {
        'url': f"https://www.youtube.com/watch?v={video_id}",
        'title': data['title'],
        'cover': data['thumbnails']['medium']['url'],
    }
