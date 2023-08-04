import datetime as dt
import isodate

from src.APImixin import APIMixin


class PlayList(APIMixin):
    def __init__(self, playlist_id):
        self.__playlist_id = playlist_id
        self._init_from_api()

    def _init_from_api(self):
        playlist_info = self.get_service().playlists().list(id=self.__playlist_id, part='snippet',
                                                          ).execute()
        self.title = playlist_info['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={self.__playlist_id}'

    @property
    def total_duration(self):
        video_response = self._get_playlist_videos()

        duration = dt.timedelta()
        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration += isodate.parse_duration(iso_8601_duration)

        return duration

    def show_best_video(self):
        video_response = self._get_playlist_videos()

        max_likes = 0
        video_id = ''
        for video in video_response['items']:
            like_count = int(video['statistics']['likeCount'])
            if like_count > max_likes:
                max_likes = like_count
                video_id = video['id']
        return f'https://youtu.be/{video_id}'

    def _get_playlist_videos(self):
        playlist_videos = self.get_service().playlistItems().list(playlistId=self.__playlist_id,
                                                           part='contentDetails',maxResults=50,).execute()
        video_ids = [video['contentDetails']['videoId']
                     for video in playlist_videos['items']]

        video_response = self.get_service().videos().list(part='contentDetails,statistics',
                                                           id=','.join(video_ids)).execute()
        return video_response

