# 导包
import logging
import unittest
from parameterized import parameterized
import app
from api.Department_Api import DepartmentApi
from api.Login_Api import LoginApi
from utils import read_data

# 创建测试类
class Test_Department(unittest.TestCase):

    # 实例级别方法
    def setUp(self):
        self.login_dep = LoginApi()
        self.dep_url = DepartmentApi()

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

    # 增加部门测试用例
    @parameterized.expand(read_data(app.BASER_MULU + "/data/login_department.json", "dep_add"))
    def test_02_add(self,name,code,manager,introduce,message):
        data = {
                    "name":name,
                    "code":code,
                    "manager":manager,
                    "introduce":introduce
                }
        res = self.dep_url.dep_add(data,app.HEADERS)
        # 日志输出
        logging.info("员工增加结果:{}".format(res.json()))
        # 获取员工id
        app.DEPARTMENT_ID = res.json().get("data").get("id")
        print(app.DEPARTMENT_ID)
        # 断言
        self.assertIn(message,res.json().get("message"))

    # 修改部门测试用例
    @parameterized.expand(read_data(app.BASER_MULU + "/data/login_department.json", "dep_updata"))
    def test_03_updata(self, name, message):
        data = {
            "name": name
        }
        res = self.dep_url.dep_updata(app.DEPARTMENT_ID,data, app.HEADERS)
        # 日志输出
        logging.info("部门修改结果:{}".format(res.json()))
        # 断言
        self.assertIn(message, res.json().get("message"))

    # 查询部门测试用例
    def test_04_select(self):
        res = self.dep_url.dep_select(app.DEPARTMENT_ID,app.HEADERS)
        # 日志输出
        logging.info("部门查询结果:{}".format(res.json()))

    # 删除部门测试用例
    def test_05_delete(self):
        res = self.dep_url.dep_delete(app.DEPARTMENT_ID,app.HEADERS)
        # 日志输出
        logging.info("删除部门结果:{}".format(res.json()))