import requests

url = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'
phonen = input('phone number: ')

pnd = {'cellphone': f'{phonen}'}

req = requests.post(url, json= pnd)

print(req.text)

