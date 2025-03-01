from typing import override
from itv import ITV


class TVOff(ITV):
    def __init__(self, prev_state:ITV):
        self.prev_state = prev_state

    @override
    def turn_on(self):
        print (f"TV on {self.prev_state.__class__.__name__} channel")
        return self.prev_state

    @override
    def news_channel(self):
        from tv_news import TVNews
        print ("Welcome to the news channel")
        return TVNews()

    @override
    def sports_channel(self):
        from tv_sports import TVSports
        print("Welcome to the sports channel")
        return TVSports()

    @override
    def movies_channel(self):
        from tv_movies import TVMovies
        print("Welcome to the movies channel")
        return TVMovies()

    @override
    def turn_off(self):
        print("TV is already OFF")
        return self