import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.video_count = self.channel["items"][0]["statistics"]["videoCount"]
        self.url = f'https://www.youtube.com/channel/{self.__channel_id}'
        self.id = self.channel["items"][0]["id"]
        self.description = self.channel["items"][0]["snippet"]["description"]
        self.subscriberCount = self.channel["items"][0]["statistics"]["subscriberCount"]
        self.viewCount = self.channel["items"][0]["statistics"]["viewCount"]

    def __str__(self) -> str:
        """ возвращающает название и ссылку на канал по шаблону <название_канала> (<ссылка_на_канал>) """
        return f"{self.title} ({self.url})"

    def __add__(self, other) -> int:
        """ возвращающает сумму сложения """
        return int(self.subscriberCount) + int(other.subscriberCount)

    def __sub__(self, other) -> int:
        """ возвращающает разность вычитания """
        return int(self.subscriberCount) - int(other.subscriberCount)

    def __eq__(self, other) -> bool:
        """ Возвращает True или False по числу подписчиков """
        return self.subscriberCount == other.subscriberCount

    def __lt__(self, other) -> bool:
        """ Возвращает True или False, по числу подписчиков """
        return self.subscriberCount < other.subscriberCount

    def __le__(self, other) -> bool:
        """ Возвращает True или False, по числу подписчиков """
        return self.subscriberCount <= other.subscriberCount

    def __gt__(self, other) -> bool:
        """ Возвращает True или False, по числу подписчиков """
        return self.subscriberCount > other.subscriberCount

    def __ge__(self, other) -> bool:
        """ Возвращает True или False, по числу подписчиков """
        return self.subscriberCount >= other.subscriberCount

    @property
    def channel_id(self) -> str:
        """ Возвращаем id канала. """
        return self.__channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel))

    @classmethod
    def get_service(cls):
        """ Возвращает объект для работы с YouTube API. """
        return cls.youtube

    def to_json(self, filename: str) -> None:
        """ Запись атрибутов в файл 'moscowpython.json'. """
        channel_info = {"title": self.title,
                        "channel_id": self.__channel_id,
                        "description": self.description,
                        "url": self.url,
                        "count_subscriberCount": self.subscriberCount,
                        "video_count": self.video_count,
                        "count_views": self.viewCount}
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(channel_info, file, indent=4, ensure_ascii=False)
