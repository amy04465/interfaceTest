#!/usr/bin/env python3
# coding=utf-8

# -*- coding: utf-8 -*-

# @Time: 18/11/10 上午12:03

# author: amy.liu

import unittest
import paramunittest
import readConfig as readConfig
from common import Log as Log
from common import common
from common import configHttp as ConfigHttp

loginCase_xls = common.get_xls("loginCase.xlsx", "login")
localReadConfig = readConfig.ReadConfig()
configHttp = ConfigHttp.ConfigHttp()
info = {}


@paramunittest.parametrized(*loginCase_xls)
class Login(unittest.TestCase):
    '''
    u'登录
    '''
    def setParameters(self, case_name, method,
                      username, password, returnUrl,
                      isremember,result, code, msg):
        """
        set params
        :param case_name:
        :param method:
        :param username:
        :param password:
        :param returnUrl:
        :param isremember
        :param result:
        :param code:
        :param msg:
        :return:
        """
        self.case_name = str(case_name)
        self.method = str(method)
        self.username = str(username)
        self.password = str(password)
        self.returnUrl = str(returnUrl)
        self.isremember = str(isremember)
        self.result = str(result)
        self.code = str(code)
        self.msg = str(msg)
        self.return_json = None
        self.info = None

    def description(self):
        """
        test report description
        :return:
        """
        return self.case_name

    def setUp(self):
        """
        :return:
        """
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()
        print(self.case_name+"  <<<<测试开始前准备")

    def testLogin(self):
        """
        test body
        :return:
        """
        # set url
        self.url = common.get_url_from_xml('login')
        configHttp.set_url_login(self.url)
        print("第一步：设置url  "+self.url)

        # set data -- post请求,请求体data必须的; get请求,参数params拼接在URL后面,有的话需要设置
        data = {"username": self.username, "password": self.password, "returnUrl": self.returnUrl, "isremember": self.isremember}
        configHttp.set_data(data)
        print("第三步：设置发送请求的参数")

        # test interface
        self.return_json = configHttp.post()
        method = str(self.return_json.request)[int(str(self.return_json.request).find('['))+1:int(str(self.return_json.request).find(']'))]
        print("第四步：发送请求\n\t\t请求方法："+method)

        # check result
        self.checkResult()
        print("第五步：检查结果")

    def tearDown(self):
        """
        :return:
        """
        pass
        self.log.build_case_line(self.case_name, str(self.info['code']), self.info['message'])
        print(self.case_name + "  <<<<测试结束，输出log完结\n\n")

    def checkResult(self):
        """
        check test result
        :return:
        """
        self.info = self.return_json.json()
        # show return message
        common.show_return_msg(self.return_json)
        self.assertEqual(self.code, str(self.info['code']))
        self.assertEqual(self.msg, str(self.info['message']))

