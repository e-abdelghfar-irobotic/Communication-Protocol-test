import requests
import json
import time
from random import choice
from string import ascii_uppercase 
api_url = "http://127.0.0.1:5000/order"
todo = {"id":4213423552,"status": f"{''.join(choice(ascii_uppercase) for i in range(3680100))}"}
start=time.perf_counter()
response = requests.post(api_url, json=todo)
# response = requests.get(api_url+'/423552')
print(f" estimated time {time.perf_counter()-start}")
# 

# response = requests.put(api_url+'/423552')

