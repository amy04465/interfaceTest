# Created by AmyLiu on 18/11/1

import unittest
import paramunittest
import readConfig as readConfig
from common import Log as Log
from common import common
from common import configHttp as ConfigHttp

loginUser_xls = common.get_xls("userCase.xlsx", "loginuser")
localReadConfig = readConfig.ReadConfig()
configHttp = ConfigHttp.ConfigHttp()
info = {}


@paramunittest.parametrized(*loginUser_xls)
class Login(unittest.TestCase):
    def setParameters(self, case_name, method, key, phoneno, cardnum, result, code, msg):
        """
        set params
        :param case_name:
        :param method:
        :param key:
        :param phoneno:
        :param cardnum:
        :param result:
        :param code:
        :param msg:
        :return:
        """
        self.case_name = str(case_name)
        self.method = str(method)
        self.key = str(key)
        self.phoneno = str(phoneno)
        self.cardnum = str(cardnum)
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
        print(self.case_name+"测试开始前准备")

    def testLogined(self):
        """
        test body
        :return:
        """
        # set url
        self.url = common.get_url_from_xml('loginUser')
        configHttp.set_url(self.url)
        print("第一步：设置url  "+self.url)

        # set params
        data = {"phoneno": self.phoneno, "cardnum": self.cardnum, "key": self.key}
        configHttp.set_data(data)
        print("第三步：设置发送请求的参数")

        # test interface
        self.return_json = configHttp.get()
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
        self.log.build_case_line(self.case_name, str(self.info['error_code']), self.info['reason'])
        print("测试结束，输出log完结\n\n")

    def checkResult(self):
        """
        check test result
        :return:
        """
        self.info = self.return_json.json()
        # show return message
        common.show_return_msg(self.return_json)
        if self.result == '0':
            self.assertEqual(str(self.info['error_code']), self.code)

