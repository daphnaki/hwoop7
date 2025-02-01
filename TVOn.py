from typing import override
from TVInterface import TVInterface

class TVOn(TVInterface):
    def __init__(self,prev_state:TVInterface):
        self.prev_state = prev_state

    @override
    def turn_on(self):
        print (f"tv is already on {self.prev_state.__class__.__name__} channel")
        return self

    @override
    def news_channel(self):
        from TVNews import TVNews
        print ("Welcome to the news channel")
        return TVNews()

    @override
    def sports_channel(self):
        from TVSports import TVSports
        print("Welcome to the sports channel")
        return TVSports()

    @override
    def movies_channel(self):
        from TVMovies import TVMovies
        print("Welcome to the movies channel")
        return TVMovies()

    @override
    def turn_off(self):
        from TVOff import TVOff
        print("TV is now OFF")
        return TVOff(self.prev_state)