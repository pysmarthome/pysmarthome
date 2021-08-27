import json
import requests

method_map = {
    'post': requests.post,
    'get': requests.get,
}

def request(addr, api_key, method='get', payload={}):
    data = method_map[method](
        addr,
        headers={
            'Authorization': api_key,
            'Content-Type': 'application/json',
        },
        data=json.dumps(payload),
    )
    return json.loads(data.content)
