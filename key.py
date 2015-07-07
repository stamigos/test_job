__author__ = 'amigos'
from collections import defaultdict
import binascii
from hashlib import md5
import base64

d = {'ik_co_id': '55964b5d3b1eaf522d8b456c',
     'ik_pm_no': 'ID_4233',
     'ik_am': '1.44'}

str = d['ik_am'] + ':' + d['ik_co_id'] + ':' + d['ik_pm_no'] + ':' + '5MJ7Byzz5Q0tJhcT'
#m = md5(str.encode())
#value = m.hexdigest
#print m.hexdigest()
#print base64.encodestring(value)
md5_string = md5(str).hexdigest()
print md5_string
print binascii.b2a_base64(md5_string)[:-1]
#print binascii.b2a_base64(m)[:-1]
