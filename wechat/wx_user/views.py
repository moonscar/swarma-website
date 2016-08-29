# -*- coding: utf8 -*-
"""微信登陆相关方法"""

from flask import Markup, redirect, request, jsonify
import requests

from weixin.client import WeixinAPI
from weixin.oauth2 import OAuth2AuthExchangeError

from settings import APP_ID, APP_SECRET, REDIRECT_URI, RECIEVED_URL
from wx_user.model import UsersWeixin
from . import wx_user
from run import app


def check_user(third_id):
    '''根据第三方id检查关联表中是否存在当前用户，目前根据openid检查'''
    user_info = UsersWeixin.query.filter_by(openid=weixin_id)
    if user_info.count():
        return True
    else:
        return False


@wx_user.route("/authorization")
def authorization():
    '''用户验证'''
    code = request.args.get('code')
    api = WeixinAPI(appid=APP_ID,
                    app_secret=APP_SECRET,
                    redirect_uri=REDIRECT_URI)
    auth_info = api.exchange_code_for_access_token(code=code)
    api = WeixinAPI(access_token=auth_info['access_token'])
    resp = api.user(openid=auth_info['openid'])

    with app.test_request_context():
        if check_user(auth_info['openid']):
            requests.post(data=resp)
        else:
            requests.put(data=resp)

    return jsonify(code=0)


@wx_user.route("/login")
def login():
    '''获取用户信息'''
    api = WeixinAPI(appid=APP_ID,
                    app_secret=APP_SECRET,
                    redirect_uri=REDIRECT_URI)
    redirect_uri = api.get_authorize_login_url(scope=("snsapi_login",))
    return redirect(redirect_uri)


@wx_user.route("/test")
def hello():
    '''测试方法'''
    return Markup('<a href="%s">weixin login!</a>') % '/login'
