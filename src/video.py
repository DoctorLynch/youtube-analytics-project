from src.APImixin import APIMixin


class Video(APIMixin):

    def __init__(self, id_video):
        self.__id_video = id_video
        self._init_from_api()

    def _init_from_api(self):
        try:
            video_response = self.get_service().videos().list(
                part='snippet,statistics', id=self.__id_video).execute()

            self.title = video_response['items'][0]['snippet']['title']
            self.url = f'https://www.youtube.com/channel/{self.__id_video}'
            self.view_count = video_response['items'][0]['statistics']['viewCount']
            self.like_count = video_response['items'][0]['statistics']['likeCount']
        except IndexError:
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None





    def __str__(self):
        return self.__id_video


class PLVideo(Video):
    def __init__(self, id_video, id_playlist):
        super().__init__(id_video)
        self.id_playlist = id_playlist







