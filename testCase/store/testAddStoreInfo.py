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
    def setParameters(self, case_name, method, address, area_code,
                      city_code, complete_date, lat, lng, project_code,
                      project_name, province_code, status, store_name,
                      store_property, tele_phone, result, code, msg):

        """
        set params
        :param case_name:
        :param method:
        :param address:
        :param area_code:
        :param city_code:
        :param complete_date
        :param lat:
        :param lng:
        :param project_code:
        :param project_name:
        :param province_code:
        :param status:
        :param store_name:
        :param store_property:
        :param tele_phone:
        :param result:
        :param code:
        :param msg:
        :return:
        """
        self.case_name = str(case_name)
        self.method = str(method)
        self.address = str(address)
        self.area_code = str(area_code)
        self.city_code = str(city_code)
        self.complete_date = str(complete_date)
        self.lat = str(lat)
        self.lng = str(lng)
        self.project_code = str(project_code)
        self.project_name = str(project_name)
        self.province_code = str(province_code)
        self.status = str(status)
        self.store_name = str(store_name)
        self.store_property = str(store_property)
        self.tele_phone = str(tele_phone)
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
        token = localReadConfig.get_headers("token")
        configHttp.set_headers(token)

        # set data -- post请求,请求体data必须的; get请求,参数params拼接在URL后面,有的话需要设置
        data = {"address": self.address, "area_code": self.area_code,
                "city_code": self.city_code, "complete_date": self.complete_date,
                "lat": self.lat, "lng": self.lng,
                "project_code": self.project_code, "project_name": self.project_name,
                "status": self.status, "store_name": self.store_name,
                "store_property": self.store_property, "tele_phone": self.tele_phone}
        configHttp.set_data(data)
        print("第三步：设置发送请求的参数")

        # test interface
        self.return_json = configHttp.post()
        method = str(self.return_json.request)[int(str(self.return_json.request).find('['))+1:int(str(self.return_json.request).find(']'))]
        print("第四步：发送请求\n\t\t请求方法："+method)

        # check result
        self.checkResult()
        print("第五步：检查结果")

        # get store code from response
        storeCode = self.info['data']
        print("获取门店编码 " + storeCode)

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
    #
    # def getStoreCode(self):
    #     """
    #     :return:
    #     """
    #     storeCode = self.info['data']
    #     return  storeCode
