__author__ = 'amigos'
from flask import render_template, Blueprint, request
from library import app

shop_page = Blueprint('shop', __name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/successful')
def successful():
    ik_co_id = request.args['ik_co_id']
    ik_inv_id = request.args['ik_inv_id']
    ik_inv_st = request.args['ik_inv_st']
    ik_inv_crt = request.args['ik_inv_crt']
    ik_inv_prc = request.args['ik_inv_prc']
    ik_pm_no = request.args['ik_pm_no']
    ik_pw_via = request.args['ik_pw_via']
    ik_am = request.args['ik_am']
    ik_co_rfn = request.args['ik_co_rfn']
    ik_ps_price = request.args['ik_ps_price']
    ik_cur = request.args['ik_cur']
    ik_desc = request.args['ik_desc']
    return render_template('successful.html', params=dict(ik_co_id=ik_co_id,
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
                           ik_desc=ik_desc)
                           )


@app.route('/fail')
def fail():
    ik_co_id = request.args['ik_co_id']
    ik_inv_id = request.args['ik_inv_id']
    ik_inv_st = request.args['ik_inv_st']
    ik_inv_crt = request.args['ik_inv_crt']
    ik_inv_prc = request.args['ik_inv_prc']
    ik_pm_no = request.args['ik_pm_no']
    ik_pw_via = request.args['ik_pw_via']
    ik_am = request.args['ik_am']
    ik_co_rfn = request.args['ik_co_rfn']
    ik_ps_price = request.args['ik_ps_price']
    ik_cur = request.args['ik_cur']
    ik_desc = request.args['ik_desc']
    return render_template('fail.html', params=dict(ik_co_id=ik_co_id,
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
                           ik_desc=ik_desc)
                           )


@app.route('/pending')
def pending():
    ik_co_id = request.args['ik_co_id']
    ik_inv_id = request.args['ik_inv_id']
    ik_inv_st = request.args['ik_inv_st']
    ik_inv_crt = request.args['ik_inv_crt']
    ik_inv_prc = request.args['ik_inv_prc']
    ik_pm_no = request.args['ik_pm_no']
    ik_pw_via = request.args['ik_pw_via']
    ik_am = request.args['ik_am']
    ik_co_rfn = request.args['ik_co_rfn']
    ik_ps_price = request.args['ik_ps_price']
    ik_cur = request.args['ik_cur']
    ik_desc = request.args['ik_desc']
    return render_template('pending.html', params=dict(ik_co_id=ik_co_id,
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
                           ik_desc=ik_desc)
                           )