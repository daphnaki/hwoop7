from typing import override
from itv import ITV


class TVMovies(ITV):

    @override
    def turn_on(self):
        print("TV on movies channel")
        return self

    @override
    def news_channel(self):
        from tv_news import TVNews
        print ("Switch to news channel")
        return TVNews()

    @override
    def sports_channel(self):
        from tv_sports import TVSports
        print ("Switch to sports channel")
        return TVSports()

    @override
    def movies_channel(self):
        print("TV on movies channel")
        return self

    @override
    def turn_off(self):
        from tv_off import TVOff
        print("TV is now off")
        return TVOff(TVMovies())