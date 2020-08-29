#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020-08-29 23:51
# @Author : Curry
# @Site : https://github.com/coolbreeze2
# @File : views.py
# @Software: PyCharm
from flask import Blueprint,render_template

blue=Blueprint("blue",__name__)

def init_blue(app):
    app.register_blueprint(blue)


@blue.route("/")
def index():
    return render_template('index.html')

@blue.route("/login")
def login():
    return render_template('login.html')

@blue.route("/register")
def register():
    return render_template('register.html')
