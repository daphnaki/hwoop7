from typing import override
from TVInterface import TVInterface


class TVSports(TVInterface):

    @override
    def turn_on(self):
        from TVOn import TVOn
        print ("TV is already ON")
        return TVOn(TVSports())

    @override
    def news_channel(self):
        from TVNews import TVNews
        print ("Welcome to the news channel")
        return TVNews()

    @override
    def sports_channel(self):
        print ("TV is already on sports channel")
        return self

    @override
    def movies_channel(self):
        from TVMovies import TVMovies
        print("Welcome to the movies channel")
        return TVMovies()

    @override
    def turn_off(self):
        from TVOff import TVOff
        print ("TV is now off")
        return TVOff(self)