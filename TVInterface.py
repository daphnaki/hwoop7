from abc import ABC, abstractmethod

class TVInterface(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def news_channel(self):
        pass

    @abstractmethod
    def sports_channel(self):
        pass

    @abstractmethod
    def movies_channel(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

