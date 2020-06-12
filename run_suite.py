# 导包
import unittest

from BeautifulReport import BeautifulReport

import app

# 创建测试套件
loader = unittest.TestLoader().discover(app.BASER_MULU + '/script',pattern='test*.py')

# 定义报告名称
file_name = "ihrm_department.html"

# 运行并生成测试报告
BeautifulReport(loader).report(filename=file_name,description="接口测试报告",log_path=app.BASER_MULU + '/report')