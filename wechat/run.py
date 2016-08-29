# from flask import Flask, Markup, redirect, request, jsonify

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from wx_user import wx_user


app = Flask(__name__, instance_relative_config=True)

app.register_blueprint(wx_user)

app.config.from_object('settings')
# app.config.from_pyfile('settings.py')

db = SQLAlchemy(app)

# from weixin.client import WeixinAPI
# from weixin.oauth2 import OAuth2AuthExchangeError

# APP_ID = 'wxa23a76af5d7d6200'
# APP_SECRET = 'd624c00563ccc593350b9c6f43edda50'
# REDIRECT_URI = 'http://swarma.org/authorization'


# @app.route("/authorization")
# def authorization():
#     code = request.args.get('code')
#     api = WeixinAPI(appid=APP_ID,
#                     app_secret=APP_SECRET,
#                     redirect_uri=REDIRECT_URI)
#     auth_info = api.exchange_code_for_access_token(code=code)
#     api = WeixinAPI(access_token=auth_info['access_token'])
#     resp = api.user(openid=auth_info['openid'])
#     return jsonify(resp)


# @app.route("/login")
# def login():
#     api = WeixinAPI(appid=APP_ID,
#                     app_secret=APP_SECRET,
#                     redirect_uri=REDIRECT_URI)
#     redirect_uri = api.get_authorize_login_url(scope=("snsapi_login",))
#     return redirect(redirect_uri)


# @app.route("/")
# def hello():
#     return Markup('<a href="%s">weixin login!</a>') % '/login'

if __name__ == "__main__":
    app.run(debug=True)
