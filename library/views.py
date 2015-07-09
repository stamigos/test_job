__author__ = 'amigos'
from flask import render_template, Blueprint, request, json, make_response
from library import app
from library.forms import PaymentFormIntercassa, PaymentFormWallet
import requests

shop_page = Blueprint('shop', __name__, template_folder='templates')


@app.route('/')
def index():
    form = PaymentFormIntercassa()
    d = {'ik_co_id': form.ik_co_id._value(), 'ik_pm_no': form.ik_pm_no._value(),
         'ik_am': form.ik_am._value(),'ik_int': form.ik_int._value(),
         'ik_act': form.ik_act._value(), 'ik_pw_via': form.ik_pw_via._value(),
         'ik_desc': form.ik_desc._value(), 'ik_sign': form.ik_sign._value()}
    print d

    r = requests.post("https://sci.interkassa.com/", data=d)
    #r1 = requests.post("https://www.walletone.com/checkout/default.aspx", data={u'paymentForm': {u'action': u'https://www.walletone.com/checkout/default.aspx', u'method': u'post', u'parameters': {u'WMI_FAIL_URL': u'https://sci.interkassa.com/paysystem/return/ps/w1/in/merchant2/ci/38028870/act/failure', u'WMI_CURRENCY_ID': 643, u'WMI_PAYMENT_AMOUNT': u'4.25', u'WMI_PTENABLED': u'WalletOneRUB', u'WMI_PAYMENT_NO': u'38028870', u'WMI_SUCCESS_URL': u'https://sci.interkassa.com/paysystem/return/ps/w1/in/merchant2/ci/38028870/act/success', u'WMI_DESCRIPTION': u'BASE64:UGF5bWVudCBOby4gSUszODAyODg3MA==', u'WMI_SIGNATURE': u'Ix+luoZifqptHVCCw36aow==', u'WMI_MERCHANT_ID': u'122651507690', u'WMI_EXPIRED_DATE': u'2015-08-06 09:04:39'}}})
    #print "r1="
    #print r1.content
    print "r="
    print r.json()
    url_IK = r.json()['resultData']['paymentForm']['action']
    ret_params = r.json()['resultData']['paymentForm']['parameters']
    # r1 = requests.post(url, json=ret_params)
    params_d = {'PAYMENT_ID': ret_params['PAYMENT_ID'], 'PAYEE_ACCOUNT': ret_params['PAYEE_ACCOUNT'],
                'PAYEE_NAME': ret_params['PAYEE_NAME'], 'PAYMENT_AMOUNT': ret_params['PAYMENT_AMOUNT'],
                'PAYMENT_UNITS': ret_params['PAYMENT_UNITS'], 'STATUS_URL': ret_params['STATUS_URL'],
                'PAYMENT_URL': ret_params['PAYMENT_URL'], 'NOPAYMENT_URL': ret_params['NOPAYMENT_URL'],
                'BAGGAGE_FIELDS': ret_params['BAGGAGE_FIELDS'], 'SUGGESTED_MEMO': ret_params['SUGGESTED_MEMO']}
    #print r1.json()
    print params_d

    form1 = PaymentFormWallet()
    d_wal = {'WMI_MERCHANT_ID': form1.WMI_MERCHANT_ID._value(), 'WMI_PAYMENT_AMOUNT': form1.WMI_PAYMENT_AMOUNT._value(),
         'WMI_CURRENCY_ID': form1.WMI_CURRENCY_ID._value(), 'WMI_DESCRIPTION': form1.WMI_DESCRIPTION._value(),
         'WMI_SUCCESS_URL': form1.WMI_SUCCESS_URL._value(), 'WMI_FAIL_URL': form1.WMI_FAIL_URL._value(),
         'WMI_PTENABLED': form1.WMI_PTENABLED._value()}
    print d_wal
    r1 = requests.post("https://wl.walletone.com/checkout/checkout/Index", data=d_wal)
    print "r1="
    print r1.json()
    return render_template('index.html', form=form, url_IK=url_IK, params=params_d)


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