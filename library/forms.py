#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'amigos'
from wtforms import Form, HiddenField
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


class PaymentFormIntercassa(Form):
    ik_co_id = HiddenField('ik_co_id', default="55964b5d3b1eaf522d8b456c")  # Идентификатор кассы
    ik_pm_no = HiddenField('ik_pm_no', default="ID_4233")  # Номер платежа
    ik_am = HiddenField('ik_am', default="1.44")  # Сумма платежа
    ik_desc = HiddenField('ik_desc', default="Payment Description")  # Описание платежа
    ik_int = HiddenField('ik_int', default="json")  # Формат ответа (web / json)
    ik_act = HiddenField('ik_act', default="process")  # Тип действия (например: payway – способ оплаты)
    ik_pw_via = HiddenField('ik_pw_via', default="perfectmoney_perfectmoney_merchant_usd")  # Платежная система (например: webmoney_webmoney_merchant_wmz)
    ik_sign = HiddenField('ik_sign', default="ScZePEArLcqaZ7QoJBKWbA==")


class PaymentFormWallet(Form):
    WMI_MERCHANT_ID = HiddenField('WMI_MERCHANT_ID', default="176742268953")
    WMI_PAYMENT_AMOUNT = HiddenField('WMI_PAYMENT_AMOUNT', default="150.00")
    WMI_CURRENCY_ID = HiddenField('WMI_CURRENCY_ID', default="980")
    WMI_DESCRIPTION = HiddenField('WMI_DESCRIPTION', default=u'Оплата демонстрационного заказа')
    WMI_SUCCESS_URL = HiddenField('WMI_SUCCESS_URL', default="https://pay-test-flask.herokuapp.com/success/")
    WMI_FAIL_URL = HiddenField('WMI_FAIL_URL', default="https://pay-test-flask.herokuapp.com/failed/")
    WMI_PTENABLED = HiddenField('WMI_PTENABLED', default='WalletOneUAH')
    WMI_SIGNATURE = HiddenField('WMI_SIGNATURE', default=get_signature([
            ('WMI_CURRENCY_ID', '980'),
            ('WMI_DESCRIPTION', u'Оплата демонстрационного заказа'),
            ('WMI_FAIL_URL', "https://pay-test-flask.herokuapp.com/failed/"),
            ('WMI_MERCHANT', '176742268953'),
            ('WMI_PAYMENT_AMOUNT', '150.00'),
            ('WMI_PTENABLED', 'WalletOneUAH'),
            ('WMI_SUCCESS_URL', 'https://pay-test-flask.herokuapp.com/success/')],
            '635d646a70424854455169753960794a7268757450637736395243'))#"cnkCh6zc9oVy6YawaQldvA==")
