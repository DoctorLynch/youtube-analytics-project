from src.APImixin import APIMixin


class Video(APIMixin):

    def __init__(self, id_video):
        self.__id_video = id_video
        self._init_from_api()

    def _init_from_api(self):
        video_response = self.get_service().videos().list(
            part='snippet,statistics', id=self.__id_video).execute()

        self.title = video_response['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/channel/{self.__id_video}'
        self.view_count = video_response['items'][0]['statistics']['viewCount']
        self.like_count = video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, id_video, id_playlist):
        super().__init__(id_video)
        self.id_playlist = id_playlist


video1 = Video('AWX4JnAnjBE')  # 'AWX4JnAnjBE' - это id видео из ютуб
video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
print(str(video1))
print(str(video2))






