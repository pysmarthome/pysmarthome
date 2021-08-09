from flask import request
from flask_restful import Resource
import asyncio
import json

class LightsResource(Resource):
    def __init__(self, devices):
        self.tasks = []
        self.devices = devices


    def post(self):
        action = request.json['action']
        for dev in self.devices:
            self.tasks.append(asyncio.to_thread(
                dev.trigger_action,
                action,
            ))

        asyncio.set_event_loop(asyncio.SelectorEventLoop())
        asyncio.get_event_loop().run_until_complete(
            asyncio.gather(*self.tasks)
        )
        return 200
