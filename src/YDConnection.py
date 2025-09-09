import requests

class YDConnection:
    """Класс для подключения к Yandex Disk API"""

    BASE_URL = 'https://cloud-api.yandex.net'

    def __init__(self, token: str):
        self.__token = token
        self.__headers = {'Authorization': f"OAuth {self.__token}"}


    def create_folder(self, path: str) -> bool:
        """Метод создания папки"""
        try:
            response = requests.put(f'{self.BASE_URL}/v1/disk/resources', params={'path': path}, headers=self.__headers)
            if response.status_code in [201, 409]:
                return True
            else:
                return False
        except:
            return False


    def upload_from_web(self, url: str, path: str = '') -> bool:
        """Метод сохранения файла из интернета"""
        upload_url = f'{self.BASE_URL}/v1/disk/resources/upload'
        params = {
            'url': url,
            'path': path
        }
        try:
            response = requests.post(upload_url, params=params, headers=self.__headers)
            response.raise_for_status()
            return True
        except:
            return False