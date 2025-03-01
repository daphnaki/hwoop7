from typing import override
from itv import ITV


class TVNews(ITV):

    @override
    def turn_on(self):
        print ("TV on news channel")
        return self

    @override
    def news_channel(self):
        print ("TV on news channel")
        return self

    @override
    def sports_channel(self):
        from tv_sports import TVSports
        print("Switch to sports channel")
        return TVSports()

    @override
    def movies_channel(self):
        from tv_movies import TVMovies
        print ("Switch to movies channel")
        return TVMovies()

    @override
    def turn_off(self):
        from tv_off import TVOff
        print ("TV is now off")
        return TVOff(TVNews())