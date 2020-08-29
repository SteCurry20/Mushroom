#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020-08-27 15:43
# @Author : Curry
# @Site : https://github.com/coolbreeze2
# @File : settings.py
# @Software: PyCharm

def get_db_url(dbinfo):
    engine=dbinfo.get("ENGINE")
    driver=dbinfo.get("DRIVER")
    user=dbinfo.get("USER")
    password=dbinfo.get("PASSWORD")
    host=dbinfo.get("HOST")
    port=dbinfo.get("PORT")
    name=dbinfo.get("NAME")


    return "{}+{}://{}:{}@{}:{}/{}".format(engine,driver,user,password,host,port,name)
class  Config:
    TESTING=False

    DEBUG=False

    SQLALCHEMY_TRACK_MODIFICATIONS=False



class DevelopConfig(Config):

    DEBUG = True

    dbinfo={
        "ENGINE":"mysql",
        "DRIVER":"pymsql",
        "USER":"root",
        "PASSWORD":"139739",
        "HOST":"localhost",
        "PORT":3306,
        "NAME":"new_shop"
    }

    SQLALCHEMY_DATABASE_URI=get_db_url(dbinfo)


class TestingConfig(Config):
    TESTING = True

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymsql",
        "USER": "root",
        "PASSWORD": "139739",
        "HOST": "localhost",
        "PORT": 3306,
        "NAME": "new_shop"
    }

    SQLALCHEMY_DATABASE_URI = get_db_url(dbinfo)


class StagingConfig(Config):

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymsql",
        "USER": "root",
        "PASSWORD": "139739",
        "HOST": "localhost",
        "PORT": 3306,
        "NAME": "new_shop"
    }

    SQLALCHEMY_DATABASE_URI = get_db_url(dbinfo)


class ProductConfig(Config):
    DEBUG = True

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymsql",
        "USER": "root",
        "PASSWORD": "139739",
        "HOST": "localhost",
        "PORT": 3306,
        "NAME": "mushroom"
    }

    SQLALCHEMY_DATABASE_URI = get_db_url(dbinfo)

envs={
    "develop":DevelopConfig,
    "testing":TestingConfig,
    "staging":StagingConfig,
    "product":ProductConfig,
    "default":DevelopConfig
}