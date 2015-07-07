__author__ = 'amigos'
from flask import render_template, Blueprint, request, json
from library import app
from library.forms import PaymentForm
import requests

shop_page = Blueprint('shop', __name__, template_folder='templates')


@app.route('/')
def index():
    form = PaymentForm()
    d = {'ik_co_id': form.ik_co_id._value(), 'ik_pm_no': form.ik_pm_no._value(), 'ik_am': form.ik_am._value(),
         'ik_int': form.ik_int._value(), 'ik_loc': form.ik_loc._value(), 'ik_enc': form.ik_enc._value(),
         'ik_act': form.ik_act._value(), 'ik_pw_via': form.ik_pw_via._value(), 'ik_desc': form.ik_desc._value()}
    print d

    #r = requests.post("https://sci.interkassa.com/", data=d)
    #resp = r.text
    #print resp
    return render_template('index.html', form=form)


@app.route('/successful')
def successful():
    ik_co_id = request.args.get['ik_co_id']
    ik_inv_id = request.args.get['ik_inv_id']
    ik_inv_st = request.args.get['ik_inv_st']
    ik_inv_crt = request.args.get['ik_inv_crt']
    ik_inv_prc = request.args.get['ik_inv_prc']
    ik_pm_no = request.args.get['ik_pm_no']
    ik_pw_via = request.args.get['ik_pw_via']
    ik_am = request.args.get['ik_am']
    ik_co_rfn = request.args.get['ik_co_rfn']
    ik_ps_price = request.args.get['ik_ps_price']
    ik_cur = request.args.get['ik_cur']
    ik_desc = request.args.get['ik_desc']
    return render_template('successful.html', ik_co_id=ik_co_id,
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


@app.route('/fail')
def fail():
    ik_co_id = request.args.get['ik_co_id']
    ik_inv_id = request.args.get['ik_inv_id']
    ik_inv_st = request.args.get['ik_inv_st']
    ik_inv_crt = request.args.get['ik_inv_crt']
    ik_inv_prc = request.args.get['ik_inv_prc']
    ik_pm_no = request.args.get['ik_pm_no']
    ik_pw_via = request.args.get['ik_pw_via']
    ik_am = request.args.get['ik_am']
    ik_co_rfn = request.args.get['ik_co_rfn']
    ik_ps_price = request.args.get['ik_ps_price']
    ik_cur = request.args.get['ik_cur']
    ik_desc = request.args.get['ik_desc']
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


@app.route('/pending')
def pending():
    ik_co_id = request.args.get['ik_co_id']
    ik_inv_id = request.args.get['ik_inv_id']
    ik_inv_st = request.args.get['ik_inv_st']
    ik_inv_crt = request.args.get['ik_inv_crt']
    ik_inv_prc = request.args.get['ik_inv_prc']
    ik_pm_no = request.args.get['ik_pm_no']
    ik_pw_via = request.args.get['ik_pw_via']
    ik_am = request.args.get['ik_am']
    ik_co_rfn = request.args.get['ik_co_rfn']
    ik_ps_price = request.args.get['ik_ps_price']
    ik_cur = request.args.get['ik_cur']
    ik_desc = request.args.get['ik_desc']
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