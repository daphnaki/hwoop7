from typing import override
from TVInterface import TVInterface


class TVMovies(TVInterface):

    @override
    def turn_on(self):
        from TVOn import TVOn
        print ("TV is already on movies channel")
        return TVOn(TVMovies())

    @override
    def news_channel(self):
        from TVNews import TVNews
        print ("Welcome to the news channel")
        return TVNews()

    @override
    def sports_channel(self):
        from TVSports import TVSports
        print ("Welcome to the sports channel")
        return TVSports()

    @override
    def movies_channel(self):
        print("You already watching the movies channel")
        return self

    @override
    def turn_off(self):
        from TVOff import TVOff
        print("TV is now off")
        return TVOff(self)