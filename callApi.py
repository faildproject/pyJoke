import requests

r =requests.get('http://192.168.178.39:5000/joke-api?language=de')
print (r.text)