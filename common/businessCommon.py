#!/usr/bin/env python3
# coding=utf-8

# -*- coding: utf-8 -*-

# @Time: 18/11/10 上午12:03

# author: amy.liu

from common import common
from common import configHttp
import readConfig as readConfig

localReadConfig = readConfig.ReadConfig()
localConfigHttp = configHttp.ConfigHttp()
localLogin_xls = common.get_xls("loginCase.xlsx", "login")


# login
def login():
    """
    login
    :return: token
    """
    # set url
    url = common.get_url_from_xml('login')
    localConfigHttp.set_url_login(url)

    # set data - 请求体
    data = {"username": localLogin_xls[0][2],
            "password": localLogin_xls[0][3],
            "returnUrl": localLogin_xls[0][4],
            "isremember": localLogin_xls[0][5]}

    localConfigHttp.set_data(data)

    # login
    response = localConfigHttp.post().json()
    # cookie = localConfigHttp.post().cookies
    # print(cookie)
    token = common.get_token_from_data(response)
    print(u'获取到的token: ' + token)
    return token


# logout
# def logout(token):
#     """
#     logout
#     :param token: login token
#     :return:
#     """
#     # set url
#     url = common.get_url_from_xml('logout')
#     localConfigHttp.set_url(url)
#
#     # set header
#     header = {'token': token}
#     localConfigHttp.set_headers(header)
#
#     # logout
#     localConfigHttp.get()
#
#
