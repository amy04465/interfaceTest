#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# @Time: 18/11/10 下午9:19

# @FileName: testAddStoreInfo.py

# author: amy.liu

import unittest
import paramunittest
import readConfig as readConfig
from common import Log as Log
from common import common
from common import configHttp as ConfigHttp
from common import businessCommon


storeCase_xls = common.get_xls("storeCase.xlsx", "testAddStoreInfo")
localReadConfig = readConfig.ReadConfig()
configHttp = ConfigHttp.ConfigHttp()
info = {}


@paramunittest.parametrized(*storeCase_xls)
class AddStoreInfo(unittest.TestCase):
    '''
    新增门店- 门店信息
    '''
    def setParameters(self, case_name, method, store_name,
                      store_property, project_code, project_name,
                      status, complete_date, tele_phone, address,
                      result, code, msg):
        """
        set params
        :param case_name:
        :param method:
        :param store_name:
        :param store_property:
        :param project_code:
        :param project_name:
        :param status:
        :param complete_date:
        :param tele_phone:
        :param address:
        :param result:
        :param code:
        :param msg:
        :return:
        """
        self.case_name = str(case_name)
        self.method = str(method)
        self.store_name = str(store_name)
        self.store_property = str(store_property)
        self.project_code = str(project_code)
        self.project_name = str(project_name)
        self.status = str(status)
        self.complete_date = str(complete_date)
        self.tele_phone = tele_phone
        self.address = str(address)
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
        # self.login_token = businessCommon.login()
        print(self.case_name+"  <<<<测试开始前准备")

    def testAddStoreInfo(self):
        """
        test body
        :return:
        """
        # set url
        self.url = common.get_url_from_xml('AddStoreInfo')
        configHttp.set_url(self.url)
        print("第一步：设置url  "+self.url)

        # set headers
        # header = {"Cookie": self.login_token}
        # token = localReadConfig.get_headers("token")
        Authori = localReadConfig.get_headers("Authorization")
        header = {"Authorization": Authori}
        configHttp.set_headers(header)

        # set data -- post请求,请求体data必须的; get请求,参数params拼接在URL后面,有的话需要设置
        data = {"store_name": self.store_name, "store_property": self.store_property,
                "project_code": self.project_code, "project_name": self.project_name,
                "status": self.status, "complete_date": self.complete_date,
                "tele_phone": self.tele_phone, "address": self.address}

        configHttp.set_data(data)
        print("第三步：设置发送请求的参数")

        # test interface
        self.return_json = configHttp.post()
        method = str(self.return_json.request)[int(str(self.return_json.request).find('['))+1:int(str(self.return_json.request).find(']'))]
        print("第四步：发送请求\n\t\t请求方法："+method)

        # check result
        self.checkResult()
        print("第五步：检查结果")

        # getStoreCodeAndSave
        self.getStoreCodeAndSave()
        print("第六步：保存结果")

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

    # get storeCode and save to txt
    def getStoreCodeAndSave(self):
        """
        get storeCode and save to txt
        :return:
        """
        storeCode = self.info['data']
        common.save_resp_to_txt("storeCode", storeCode)


