#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'amigos'
from wtforms import Form, BooleanField, TextField, HiddenField, validators


class PaymentForm(Form):
    ik_co_id = HiddenField('ik_co_id', default="55964b5d3b1eaf522d8b456c")  # Идентификатор кассы
    ik_pm_no = HiddenField('ik_pm_no', default="ID_4233")  # Номер платежа
    ik_am = HiddenField('ik_am', default="1.44")  # Сумма платежа
   # ik_curr = HiddenField('ik_curr', default="u")
    ik_desc = HiddenField('ik_desc', default="Payment Description")  # Описание платежа
    ik_int = HiddenField('ik_int', default="web")  # Формат ответа (web / json)
    ik_loc = HiddenField('ik_loc', default="en")  # Локаль
    ik_enc = HiddenField('ik_enc', default="utf-8")  # Кодировка
    ik_act = HiddenField('ik_act', default="process")  # Тип действия (например: payway – способ оплаты)
    ik_pw_via = HiddenField('ik_pw_via', default="w1_w1_merchant_rub")  # Платежная система (например: webmoney_webmoney_merchant_wmz)
