from itv import ITV


class Context:
    def __init__(self, prev_state:ITV):
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