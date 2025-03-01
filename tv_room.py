from context import Context
from tv_movies import TVMovies


if __name__ == '__main__':

    tv_room = Context(TVMovies())
    tv_room.movies_channel()
    tv_room.sports_channel()
    tv_room.news_channel()
    tv_room.news_channel()
    tv_room.turn_on()
    tv_room.turn_off()
    tv_room.turn_on()
    tv_room.news_channel()
