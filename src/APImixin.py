from googleapiclient.discovery import build

class APIMixin:
    __Api_key: str = 'AIzaSyDRERmmuEbSp6BnuDpMURlskRTjs1AcDrw'

    @classmethod
    def get_service(cls):
        service = build('youtube', 'v3', developerKey=cls.__Api_key)
        return service