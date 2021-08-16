from .db import DB
import json
import os
import asyncio
import boto3
import bson


class s3db(DB):
    def __init__(self, bucket_name='', collection_names={}, enc='json'):
        self.bucket_name = bucket_name
        self.enc = enc
        self.collection_names = collection_names
        self.collections = {}
        self.s3 = boto3.client('s3')
        self.load_collections()


    ### DO IT ASYNC!!! ###
    def load_collections(self):
        objs = self.s3.list_objects(Bucket=self.bucket_name)['Contents']
        split_exts = map(lambda o: os.path.splitext(o['Key']), objs)
        enc_filtered = filter(lambda s: s[1][1:] == self.enc, split_exts)

        for name, _ in enc_filtered:
            self.collections[name] = S3Collection(name, self.bucket_name, self.enc)
            self.collections[name].load_documents()


    def get(self, id, collection_id):
        try:
            return self.collections[collection_id].get(id)
        except Exception as e:
            raise e


    def update(self, id, collection_id, **data):
        try:
            return self.collections[collection_id].set(id, **data)
        except Exception as e:
            raise e


    def create(self, collection_id, **data):
        raise NotImplementedError('Not implemented')


class S3Collection:
    encodings = {
        'bson': {
            'loader': bson.loads,
            'dumper': bson.dumps,
        },
        'json': {
            'loader': json.loads,
            'dumper': json.dumps,
        },
    }

    def __init__(self, name, bucket_name, enc='json'):
        self.bucket_name = bucket_name
        self._name = name
        self.enc = enc
        self.s3 = boto3.client('s3')
        self.filename = f'{self.name}.{self.enc}'

    @property
    def name(self): return self._name


    @property
    def documents(self): return self._documents.values()


    @documents.setter
    def documents(self, docs): self._documents = docs


    def load_documents(self):
        body = self.s3.get_object(Bucket=self.bucket_name, Key=self.filename)['Body']
        self._documents = self.encodings[self.enc]['loader'](body.read())


    def get(self, id):
        try:
            return self._documents[id]
        except Exception as e:
            print(e)


    def set(self, id, **data):
        try:
            for k, v in data.items():
                self._documents[id][k] = v
            data = self.encodings[self.enc]['dumper'](self._documents)
            ### do it ASYNC!!! ###
            self.s3.put_object(Body=data, Bucket=self.bucket_name, Key=self.filename)
        except Exception as e:
            raise e
