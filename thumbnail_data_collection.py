import requests
import pandas as pd
import os
from dotenv import load_dotenv

class VideoEntry():
    thumbnail: str
    videoId: str
    channel: str
    views: int
    subs: int
    score: float
    
    def __init__(self) -> None:
        pass


def main():
    load_dotenv()
    
    cycles = 1
    api_key = os.getenv("API_KEY")
    df = []
    
    while cycles > 0:
        url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&type=video&key={api_key}'
        response = requests.get(url)
        json = response.json()
        
        data_list = []
        if 'items' in json:
            for item in json['items']:
                new_data = VideoEntry()
                new_data.videoId = item['id']['videoId']
                new_data.thumbnail = item['snippet']['thumbnails']['high']['url']
                new_data.channel = item['snippet']['channelId']
                data_list.append(new_data)
                
        for data in data_list:
            url = f'https://youtube.googleapis.com/youtube/v3/channels?part=snippet%2Cstatistics&id={data.channel}&key={api_key}'
            response = requests.get(url)
            channel_json = response.json()
            try: 
                data.subs = int(channel_json['items'][0]['statistics']['subscriberCount'])
                if data.subs == 0:
                    data.subs = 1
            except:
                data.subs = 1
            
            url = f'https://youtube.googleapis.com/youtube/v3/videos?part=snippet%2Cstatistics&id={data.videoId}&key={api_key}'
            response = requests.get(url)
            video_json = response.json()
            try:
                data.views = int(video_json['items'][0]['statistics']['viewCount'])
            except:
                data.views = 0
            
            view_count_score = data.views / 1000000
            view_ratio_score = data.views / data.subs / 100
            if view_count_score + view_ratio_score > 1:
                data.score = 1
            else:
                data.score = view_count_score + view_ratio_score

            if data.score > 0:  
                df.append({'thumbnail': data.thumbnail, 'score': data.score})
            
        cycles -= 1
    
    df = pd.DataFrame(df)
    df.to_csv('thumbnail_data_NEW.csv', index=False)

if __name__ == '__main__':
    main()