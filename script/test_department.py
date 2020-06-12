# 导包
import logging
import unittest

from parameterized import parameterized

import app
from api.Login_Api import LoginApi

# 创建测试类
from utils import read_data


class Test_Department(unittest.TestCase):

    # 类级别方法
    def setUpClass(cls):
        pass

    # 类级别销毁方法
    def tearDownClass(cls):
        pass

    # 实例级别方法
    def setUp(self):
        self.login_dep = LoginApi()

    # 实例级别销毁方法
    def tearDown(self):
        pass

    # 登陆测试用例
    @parameterized.expand(read_data(app.BASER_MULU + "/data/login_department.json","login"))
    def test_01_login(self,mobile,password,message):
        data = {"mobile":mobile,"password":password}
        headers = {"Content-Type":"application/json"}
        # 调用登陆请求接口
        res = self.login_dep.login_post(data,headers)
        logging.info("登陆结果是：{}".format(res.json()))

        # 获取令牌保存到全局变量
        app.HEADERS = {"Content-Type":"application/json","Authorization":res.json().data}

        # 断言
        self.assertIn(message,res.json().get("message"))