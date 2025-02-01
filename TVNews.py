from typing import override
from TVInterface import TVInterface


class TVNews(TVInterface):

    @override
    def turn_on(self):
        from TVOn import TVOn
        print ("TV is already on news channel")
        return TVOn(TVNews())

    @override
    def news_channel(self):
        print ("You already watching the news channel")
        return self

    @override
    def sports_channel(self):
        from TVSports import TVSports
        print("Welcome to the sports channel")
        return TVSports()

    @override
    def movies_channel(self):
        from TVMovies import TVMovies
        print ("Welcome to the movie channel")
        return TVMovies()

    @override
    def turn_off(self):
        from TVOff import TVOff
        print ("TV is now off")
        return TVOff(self)