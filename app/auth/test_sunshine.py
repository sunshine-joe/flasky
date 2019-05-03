#!/usr/bin python
# -*- coding: utf-8 -*-
# ************************************************************
# @File          : test_sunshine.py
# @Create Time   : 2019/5/3 12:07 PM
# @Creator       : shuzhou.zsz(shuzhou.zsz@alibaba-inc.com)
# @Modify Time   : 2019/5/3 12:07 PM
# @Modify Author : shuzhou.zsz(shuzhou.zsz@alibaba-inc.com)
# @Description   :
# ************************************************************

from . import auth

def ret_data(code=200, success=True, msg=''):
    return dict(code=code, success=success, msg=msg)


@auth.route('/addurl')
def test_add_url_for():
    from flask.json import jsonify
    return jsonify(ret_data())

