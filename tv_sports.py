from typing import override
from itv import ITV


class TVSports(ITV):

    @override
    def turn_on(self):
        print("TV on sports channel")
        return self

    @override
    def news_channel(self):
        from tv_news import TVNews
        print ("Switch to news channel")
        return TVNews()

    @override
    def sports_channel(self):
        print ("TV on sports channel")
        return self

    @override
    def movies_channel(self):
        from tv_movies import TVMovies
        print("Switch to movies channel")
        return TVMovies()

    @override
    def turn_off(self):
        from tv_off import TVOff
        print ("TV is now off")
        return TVOff(TVSports())