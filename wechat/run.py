# -*- coding: utf8 -*-
"""主文件"""
# from flask import Flask, Markup, redirect, request, jsonify

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from wx_user import wx_user


app = Flask(__name__, instance_relative_config=True)

app.register_blueprint(wx_user)

app.config.from_object('settings')

db = SQLAlchemy(app)


if __name__ == "__main__":
    app.run(debug=True)
