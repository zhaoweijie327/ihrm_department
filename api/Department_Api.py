# 导包
import requests

# 创建部门管理接口
class DepartmentApi:

    # 初始化管理url地址
    def __init__(self):
        # 查看部门组织架构和添加部门同一个地址，请求不同
        self.dep_url = "http://ihrm-test.itheima.net" + "/api/company/department"

    # 封装查看部门组织架构列表接口
    def dep_zuzhi(self,headers):
        return requests.get(url=self.dep_url,headers=headers)

    # 封装添加部门接口
    def dep_add(self,data,headers):
        return requests.post(url=self.dep_url,json=data,headers=headers)

    # 封装修改部门接口
    def dep_updata(self,dep_id,data,headers):
        url = self.dep_url +"/" + dep_id
        return requests.put(url=url,json=data,headers=headers)

    # 封装查看部门信息接口
    def dep_select(self,dep_id,headers):
        url = self.dep_url +"/" + dep_id
        return requests.get(url=url,headers=headers)

    # 封装删除部门信息接口
    def dep_delete(self,dep_id,headers):
        url = self.dep_url +"/" + dep_id
        return requests.get(url=url, headers=headers)