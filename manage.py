#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020-08-29 23:13
# @Author : Curry
# @Site : https://github.com/coolbreeze2
# @File : manage.py
# @Software: PyCharm
import os

from flask_migrate import MigrateCommand
from flask_script import Manager
from App import create_app

env=os.environ.get("FLASK_ENV") or "default"


app=create_app(env)
manager=Manager(app)

manager.add_command("db",MigrateCommand)

if __name__ == '__main__':
    manager.run()