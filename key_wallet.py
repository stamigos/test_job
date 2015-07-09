#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'amigos'
from collections import defaultdict
import binascii
from hashlib import md5


def get_signature(params, secret_key):
    """
    Base64(Byte(MD5(Windows1251(Sort(Params) + SecretKey))))
    params - list of tuples [('WMI_CURRENCY_ID', 643), ('WMI_PAYMENT_AMOUNT', 10)]
    """
    icase_key = lambda s: unicode(s).lower()

    lists_by_keys = defaultdict(list)
    for key, value in params:
        lists_by_keys[key].append(value)

    str_buff = ''
    for key in sorted(lists_by_keys, key=icase_key):
        for value in sorted(lists_by_keys[key], key=icase_key):
            str_buff += unicode(value).encode('1251')
    str_buff += secret_key
    md5_string = md5(str_buff).digest()
    return binascii.b2a_base64(md5_string)[:-1]

key = get_signature([
            ('WMI_CURRENCY_ID', '980'),
            ('WMI_DESCRIPTION', u'Оплата демонстрационного заказа'),
            ('WMI_FAIL_URL', "https://pay-test-flask.herokuapp.com/failed/"),
            ('WMI_MERCHANT', '176742268953'),
            ('WMI_PAYMENT_AMOUNT', '150.00'),
            ('WMI_PTENABLED', 'WalletOneUAH'),
            ('WMI_SUCCESS_URL', 'https://pay-test-flask.herokuapp.com/success/')],
            '635d646a70424854455169753960794a7268757450637736395243')

key1 = get_signature([
            ('WMI_CURRENCY_ID', '980'),
            ('WMI_DESCRIPTION', u'Оплата демонстрационного заказа'),
            ('WMI_MERCHANT', '176742268953'),
            ('WMI_PAYMENT_AMOUNT', '100.00')],
            '635d646a70424854455169753960794a7268757450637736395243')

print key
print key1