from typing import Any

from src.channel import Channel


class Video(Channel):
    def __init__(self, id_video: Any) -> None:
        self.id_video = id_video
        youtube = self.get_service()
        self.video = (youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails', id=self.id_video)
                      .execute())
        self.title = self.video['items'][0]['snippet']['title']
        self.url = 'https://www.youtube.com/watch?v=' + self.id_video
        self.number_view = self.video['items'][0]['statistics']['viewCount']
        self.number_likes = self.video['items'][0]['statistics']['likeCount']
        self.duration = self.video["items"][0]['contentDetails']['duration']
        self.likes_count = self.video["items"][0]["statistics"]["likeCount"]

        def __str__(self):
            return f'{self.title}'


class PLVideo(Video):
    def __init__(self, id_video: Any, play_list_id: Any) -> None:
        super().__init__(id_video)
        youtube = self.get_service()
        self.play_list_id = (youtube.playlistItems().list(playlistId=play_list_id, part='contentDetails',
                                                          maxResults=50).execute())
