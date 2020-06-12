# 导包
import requests

# 创建登陆接口类
class LoginApi:

    # 初始化管理url
    def __init__(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"

    # 封装post登陆请求
    def login_post(self,jsonData,headers):
        return requests.post(url=self.login_url,json=jsonData,headers=headers)
