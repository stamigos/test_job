__author__ = 'amigos'
import requests

r = requests.post('http://127.0.0.1:5000/callback/')

print r.text