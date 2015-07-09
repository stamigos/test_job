__author__ = 'amigos'
from flask import render_template, Blueprint, request, json, make_response
from library import app
from library.forms import PaymentFormIntercassa, PaymentFormWallet
from BeautifulSoup import BeautifulSoup
import requests


shop_page = Blueprint('shop', __name__, template_folder='templates')


@app.route('/')
def index():
    form = PaymentFormIntercassa()
    d = {'ik_co_id': form.ik_co_id._value(), 'ik_pm_no': form.ik_pm_no._value(),
         'ik_am': form.ik_am._value(),'ik_int': form.ik_int._value(),
         'ik_act': form.ik_act._value(), 'ik_pw_via': form.ik_pw_via._value(),
         'ik_desc': form.ik_desc._value(), 'ik_sign': form.ik_sign._value()}

    r = requests.post("https://sci.interkassa.com/", data=d)
    url_IK = r.json()['resultData']['paymentForm']['action']
    ret_params = r.json()['resultData']['paymentForm']['parameters']
    params_d = {'PAYMENT_ID': ret_params['PAYMENT_ID'], 'PAYEE_ACCOUNT': ret_params['PAYEE_ACCOUNT'],
                'PAYEE_NAME': ret_params['PAYEE_NAME'], 'PAYMENT_AMOUNT': ret_params['PAYMENT_AMOUNT'],
                'PAYMENT_UNITS': ret_params['PAYMENT_UNITS'], 'STATUS_URL': ret_params['STATUS_URL'],
                'PAYMENT_URL': ret_params['PAYMENT_URL'], 'NOPAYMENT_URL': ret_params['NOPAYMENT_URL'],
                'BAGGAGE_FIELDS': ret_params['BAGGAGE_FIELDS'], 'SUGGESTED_MEMO': ret_params['SUGGESTED_MEMO']}

    form1 = PaymentFormWallet()
    d_wal = {'WMI_MERCHANT_ID': form1.WMI_MERCHANT_ID._value(), 'WMI_PAYMENT_AMOUNT': form1.WMI_PAYMENT_AMOUNT._value(),
             'WMI_CURRENCY_ID': form1.WMI_CURRENCY_ID._value(), 'WMI_DESCRIPTION': form1.WMI_DESCRIPTION._value(),
             'WMI_SUCCESS_URL': form1.WMI_SUCCESS_URL._value(), 'WMI_FAIL_URL': form1.WMI_FAIL_URL._value(),
             'WMI_PTENABLED': form1.WMI_PTENABLED._value(), 'WMI_SIGNATURE': form1.WMI_SIGNATURE._value()}

    r1 = requests.post("https://wl.walletone.com/checkout/checkout/Index", data=d_wal)
    soup = BeautifulSoup(''.join(r1.text))
    inputs = soup.findAll('input', {'type': ['hidden']})
    inputs_l = []
    for inp in inputs:
        inputs_l.append({inp.get('name'): inp.get('value')})
    url_w1 = soup.find('form').get('action')
    id_w1 = soup.find('form').get('id')
    return render_template('index.html', form=form, id_w1=id_w1, inputs_l=inputs_l,
                           url_w1=url_w1, url_IK=url_IK, params=params_d)


@app.route('/results/', methods=['POST'])
def results():
    return make_response(("Payment, ok", 200, {}))


@app.route('/callback/', methods=['POST'])
def callback():
    return make_response(("Hello, world!", 200, {}))


@app.route('/successful/')
def successful():
    ik_co_id = request.args.get('ik_co_id')
    ik_inv_id = request.args.get('ik_inv_id')
    ik_inv_st = request.args.get('ik_inv_st')
    ik_inv_crt = request.args.get('ik_inv_crt')
    ik_inv_prc = request.args.get('ik_inv_prc')
    ik_pm_no = request.args.get('ik_pm_no')
    ik_pw_via = request.args.get('ik_pw_via')
    ik_am = request.args.get('ik_am')
    ik_co_rfn = request.args.get('ik_co_rfn')
    ik_ps_price = request.args.get('ik_ps_price')
    ik_cur = request.args.get('ik_cur')
    ik_desc = request.args.get('ik_desc')
    return render_template('successful.html',
                           ik_co_id=ik_co_id,
                           ik_inv_id=ik_inv_id,
                           ik_inv_st=ik_inv_st,
                           ik_inv_crt=ik_inv_crt,
                           ik_inv_prc=ik_inv_prc,
                           ik_pm_no=ik_pm_no,
                           ik_pw_via=ik_pw_via,
                           ik_am=ik_am,
                           ik_co_rfn=ik_co_rfn,
                           ik_ps_price=ik_ps_price,
                           ik_cur=ik_cur,
                           ik_desc=ik_desc
                           )


@app.route('/fail/')
def fail():
    ik_co_id = request.args.get('ik_co_id')
    ik_inv_id = request.args.get('ik_inv_id')
    ik_inv_st = request.args.get('ik_inv_st')
    ik_inv_crt = request.args.get('ik_inv_crt')
    ik_inv_prc = request.args.get('ik_inv_prc')
    ik_pm_no = request.args.get('ik_pm_no')
    ik_pw_via = request.args.get('ik_pw_via')
    ik_am = request.args.get('ik_am')
    ik_co_rfn = request.args.get('ik_co_rfn')
    ik_ps_price = request.args.get('ik_ps_price')
    ik_cur = request.args.get('ik_cur')
    ik_desc = request.args.get('ik_desc')
    return render_template('fail.html', ik_co_id=ik_co_id,
                           ik_inv_id=ik_inv_id,
                           ik_inv_st=ik_inv_st,
                           ik_inv_crt=ik_inv_crt,
                           ik_inv_prc=ik_inv_prc,
                           ik_pm_no=ik_pm_no,
                           ik_pw_via=ik_pw_via,
                           ik_am=ik_am,
                           ik_co_rfn=ik_co_rfn,
                           ik_ps_price=ik_ps_price,
                           ik_cur=ik_cur,
                           ik_desc=ik_desc
                           )


@app.route('/pending/')
def pending():
    ik_co_id = request.args.get('ik_co_id')
    ik_inv_id = request.args.get('ik_inv_id')
    ik_inv_st = request.args.get('ik_inv_st')
    ik_inv_crt = request.args.get('ik_inv_crt')
    ik_inv_prc = request.args.get('ik_inv_prc')
    ik_pm_no = request.args.get('ik_pm_no')
    ik_pw_via = request.args.get('ik_pw_via')
    ik_am = request.args.get('ik_am')
    ik_co_rfn = request.args.get('ik_co_rfn')
    ik_ps_price = request.args.get('ik_ps_price')
    ik_cur = request.args.get('ik_cur')
    ik_desc = request.args.get('ik_desc')
    return render_template('pending.html', ik_co_id=ik_co_id,
                           ik_inv_id=ik_inv_id,
                           ik_inv_st=ik_inv_st,
                           ik_inv_crt=ik_inv_crt,
                           ik_inv_prc=ik_inv_prc,
                           ik_pm_no=ik_pm_no,
                           ik_pw_via=ik_pw_via,
                           ik_am=ik_am,
                           ik_co_rfn=ik_co_rfn,
                           ik_ps_price=ik_ps_price,
                           ik_cur=ik_cur,
                           ik_desc=ik_desc
                           )