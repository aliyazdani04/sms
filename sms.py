import requests
from termcolor import colored

url = 'https://web.rubika.ir/assets/fonts/rbico.ttf'

phonen = input('phone number: ')

pnd = {'cellphone': f'{phonen}'}

while True:

      req = requests.post(url, json= pnd)

      print(colored('yes', 'red'))

