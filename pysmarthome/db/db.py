from abc import ABC, abstractmethod


class db(ABC):
    @abstractmethod
    def get(self, id, collection_id):
        pass

    @abstractmethod
    def update(self, id, collection_id, **data):
        pass

    @abstractmethod
    def create(self, collection_id, **data):
        pass
