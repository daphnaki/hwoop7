from TVInterface import TVInterface

from TVOn import TVOn
from TVMovies import TVMovies


class Context:
    def __init__(self,prev_state:TVInterface):
        self.prev_state = prev_state

    def turn_on(self):
        self.prev_state = self.prev_state.turn_on()

    def news_channel(self):
        self.prev_state = self.prev_state.news_channel()

    def sports_channel(self):
        self.prev_state = self.prev_state.sports_channel()


    def movies_channel(self):
        self.prev_state = self.prev_state.movies_channel()


    def turn_off(self):
        self.prev_state = self.prev_state.turn_off()


if __name__ == '__main__':

    tv_room = Context(TVOn(TVMovies()))
    tv_room.movies_channel()
    tv_room.sports_channel()
    tv_room.news_channel()
    tv_room.news_channel()
    tv_room.turn_on()
    tv_room.turn_off()
    tv_room.turn_on()
    tv_room.news_channel()
