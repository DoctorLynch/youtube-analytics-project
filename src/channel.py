import json

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = 'AIzaSyDRERmmuEbSp6BnuDpMURlskRTjs1AcDrw'

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel = Channel.get_service().channels().list(
            id=channel_id, part='snippet,statistics'
        ).execute()

        self.id = self.channel['items'][0]['id']
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.custom_url = self.channel['items'][0]['snippet']['customUrl']
        self.url = f'https://www.youtube.com/channel/{self.id}'
        self.subscribercount = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.view_count = self.channel['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        return int(self.subscribercount) + int(other.subscribercount) or int(self.subscribercount) == int(other.subscribercount)

    def __sub__(self, other):
        return int(self.subscribercount) - int(other.subscribercount) or int(other.subscribercount) - int(self.subscribercount)

    def __lt__(self, other):
        return int(self.subscribercount) < int(other.subscribercount)

    def __le__(self, other):
        return int(self.subscribercount) <= int(other.subscribercount)

    def __gt__(self, other):
        return int(self.subscribercount) > int(other.subscribercount)

    def __ge__(self, other):
        return int(self.subscribercount) >= int(other.subscribercount)



    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=cls.api_key)

    def to_json(self, path):
        data = self.__dict__
        del data['channel']
        with open(path, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))
