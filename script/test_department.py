# 导包
import logging
import unittest
from parameterized import parameterized
import app
from api.Login_Api import LoginApi
from utils import read_data

# 创建测试类
class Test_Department(unittest.TestCase):

    # 实例级别方法
    def setUp(self):
        self.login_dep = LoginApi()

    def tearDown(self):
        pass

    # 登陆测试用例
    @parameterized.expand(read_data(app.BASER_MULU + "/data/login_department.json","login_api"))
    def test_01_login(self,mobile,password,message):
        data = {"mobile":mobile,"password":password}
        headers = {"Content-Type":"application/json"}
        # 调用登陆请求接口
        res = self.login_dep.login_post(data,headers)
        logging.info("登陆成功结果是：{}".format(res.json()))

        # 获取令牌保存到全局变量
        app.HEADERS = {"Content-Type":"application/json","Authorization":"Bearer "+res.json().get("data")}

        # 断言
        self.assertIn(message,res.json().get("message"))
        事实上
