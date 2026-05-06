import requests

BASE_URL = "https://petstore.swagger.io/v2"

def get(endpoint, params=None):
    return requests.get(f"{BASE_URL}{endpoint}", params=params)

def post(endpoint, payload):
    return requests.post(f"{BASE_URL}{endpoint}", json=payload)

def put(endpoint, payload):
    return requests.put(f"{BASE_URL}{endpoint}", json=payload)

def delete(endpoint):
    return requests.delete(f"{BASE_URL}{endpoint}")