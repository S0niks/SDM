from abc import ABC, abstractmethod


class ABCRepository(ABC):
    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def find(self, query):
        pass
