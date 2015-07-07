__author__ = 'amigos'
import hashlib
import base64


d = {'ik_co_id': '55964b5d3b1eaf522d8b456c',
     'ik_pm_no': 'ID_4233',
     'ik_am': '1.44',
     'ik_desc': 'Payment Description'}

str = d['ik_am'] + ':' + d['ik_co_id'] + ':' + d['ik_desc'] + ':' + d['ik_pm_no'] + ':' + 'vf6j7MfrieEp7MUT'
#m = md5(str.encode())
#value = m.hexdigest
#print m.hexdigest()
#print base64.encodestring(value)
md5_string = hashlib.md5(str).digest()

print md5_string
sign = base64.encodestring(md5_string)[:-1]
print sign
print len(sign)
#print binascii.b2a_base64(m)[:-1]
