from s3db import s3db
from durc import DB


class db(DB):
    @staticmethod
    def init(config):
        return s3db(config)

    def get(self, id, collection_id):
        return s3db.get(id, collection_id)


    def get_one(self, collection_id):
        return s3db.get_one(id, collection_id)


    def get_all(self, collection_id):
        return s3db.get_all(collection_id)


    def update(self, id, collection_id, **data):
        s3db.update(id, collection_id, **data)


    def create(self, collection_id, **data):
        s3db.create(collection_id, **data)


    def delete(self, id, collection_id):
        s3db.delete(id, collection_id)
