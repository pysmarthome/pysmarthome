from .db import db
import json
import os
import asyncio
import boto3
import bson

class s3db(db):
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

    def __init__(self, config):
        configs = {
            'bucket_name': '',
            'collection_files': { 'root': 'root' },
            'encoding': 'json',
            'cache': True,
            **config,
        }

        self.cache = configs['cache']
        self.bucket_name = configs['bucket_name']
        self.encoding = configs['encoding']
        self.collection_files = configs['collection_files']

        self.collection_files_ref = {}
        for filename, collections in self.collection_files.items():
            for collection_id in collections:
                self.collection_files_ref[collection_id] = filename

        self.updated_files = []
        self.cached_files = {}

        self.aws_credentials = {}
        if 'aws_secret_access_key' in configs and \
            configs['aws_secret_access_key'] != '' and \
            'aws_access_key_id' in configs and \
            configs['aws_access_key_id'] != '':
            self.aws_credentials = {
                'aws_secret_access_key': configs['aws_secret_access_key'],
                'aws_access_key_id': configs['aws_access_key_id'],
            }

        self.s3 = boto3.client('s3', **self.aws_credentials)


    def put_s3_object(self, filename, data):
        data = self.encodings[self.encoding]['dumper'](data)
        self.s3.put_object(Body=data, Bucket=self.bucket_name, Key=filename)


    def get_s3_object(self, filename):
        print('s3 get!')
        data = self.s3.get_object(Bucket=self.bucket_name, Key=filename)['Body']
        return self.encodings[self.encoding]['loader'](data.read())


    def get(self, id, c_id):
        print('db get')
        try:
            filename = self.collection_files_ref[c_id]
            return self.get_collections(filename)[c_id][id]
        except Exception as e:
            raise e


    def update(self, id, c_id, **data):
        try:
            filename = self.collection_files_ref[c_id]
            collections = self.get_collections(filename)
            if id not in collections[c_id]:
                collections[c_id][id] = { 'id': id }
            items = data.items()
            updated = 0
            for k, v in items:
                if v != collections[c_id][id][k]:
                    collections[c_id][id][k] = v
                    updated += 1
            if updated:
                self.store_collections(filename, collections)
        except Exception as e:
            raise e


    def create(self, c_id, **data):
        try:
            id = data.pop('id')
            self.update(id, c_id, **data)
        except Exception as e:
            raise e


    def get_collections(self, filename):
        try:
            filename += f'.{self.encoding}'
            print(filename)
            if self.cache:
                if filename not in self.cached_files:
                    self.cached_files[filename] = self.get_s3_object(filename)
                print('get from cache :)')
                return self.cached_files[filename]
            return self.get_s3_object(filename)
        except Exception as e:
            raise e


    def store_collections(self, filename, data):
        filename += f'.{self.encoding}'
        try:
            print('s3 put object (cached_files none)!')
            asyncio.set_event_loop(asyncio.SelectorEventLoop())
            loop = asyncio.get_event_loop()
            loop.run_in_executor(None, self.put_s3_object, filename, data)
        except Exception as e:
            raise e


    def get_one(self, c_id):
        print('db get one')
        try:
            filename = self.collection_files_ref[c_id]
            documents = self.get_collections(filename)[c_id]
            return list(documents.values())[0]
        except Exception as e:
            raise e


    def delete(self, id, c_id):
        try:
            filename = self.collection_files_ref[c_id]
            collections = self.get_collections(filename)
            del collections[id]
            self.store_collections(filename, collections)
        except Exception as e:
            raise e
