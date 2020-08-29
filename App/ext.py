#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020-08-29 23:45
# @Author : Curry
# @Site : https://github.com/coolbreeze2
# @File : ext.py
# @Software: PyCharm
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
migrate=Migrate()

def init_ext(app):
    db.init_app(app)
    migrate.init_app(app,db)


