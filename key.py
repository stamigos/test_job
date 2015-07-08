__author__ = 'amigos'
import hashlib
import base64


d = {'ik_co_id': '55964b5d3b1eaf522d8b456c',
     'ik_pm_no': 'ID_4233',
     'ik_am': '1.44',
     'ik_desc': 'Payment Description',
     'ik_act': 'process',
     'ik_pw_via': 'perfectmoney_perfectmoney_merchant_usd',
     'ik_int': 'json'}

str_IK = d['ik_act'] + ':' + d['ik_am'] + ':' + d['ik_co_id'] + ':' + \
         d['ik_desc'] + ':' + d['ik_pm_no'] + ':' + 'test_interkassa_test_xts' + ':' + 'vf6j7MfrieEp7MUT'
#m = md5(str.encode())
#value = m.hexdigest
#print m.hexdigest()
#print base64.encodestring(value)
md5_string = hashlib.md5(str_IK).digest()

print md5_string
sign_IK = base64.encodestring(md5_string)[:-1]
print 'sign_IK=' + sign_IK
print len(sign_IK)
str_hidden_mode = d['ik_act'] + ':' + d['ik_am'] + ':' + d['ik_co_id'] + ':' + d['ik_desc'] + ':' + \
                  d['ik_int'] + ':' + d['ik_pm_no'] + ':' + d['ik_pw_via'] + ':' + 'vf6j7MfrieEp7MUT'
#print binascii.b2a_base64(m)[:-1]
md5_string2 = hashlib.md5(str_hidden_mode).digest()
sign_hidden_mode = base64.encodestring(md5_string2)[:-1]
print 'sign_hidden_mode=' + sign_hidden_mode
print len(sign_hidden_mode)
