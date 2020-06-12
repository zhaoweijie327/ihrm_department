import json
import logging
import logging.handlers
import app


def init_logging():
    # 设置日志器
    logger = logging.getLogger()
    # 设置日志等级
    logger.setLevel(level=logging.INFO)
    # 设置控制台处理器
    sf = logging.StreamHandler()
    # 设置路径保存地址
    log_path = app.BASER_MULU + "/log/ihrm_department.log"
    fh = logging.handlers.TimedRotatingFileHandler(log_path,when="M",interval=1,backupCount=3,encoding='utf-8')
    # 设置格式化器
    fmt_name = '%(asctime)s %(levelname)s [%(name)s] ' \
               '[%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    farmatter = logging.Formatter(fmt_name)
    # 将格式化器添加到文件处理器和控制台处理器
    sf.setFormatter(farmatter)
    fh.setFormatter(farmatter)
    # 将文件处理器和控制台处理器添加到日志器中
    logger.addHandler(sf)
    logger.addHandler(fh)

# 读取data文件夹中json数据
def read_data(file_path,intreface_name):
    # 定义一个空列表
    data_list = []
    # 读取数据
    with open(file_path,'r',encoding="utf-8") as file:
        # 转成json数据
        json_data = json.load(file)
        # 获取json字典的值
        json_values = json_data.get(intreface_name)
        # 添加到列表中
        data_list.append(list(json_values.values()))
    # 返回列表数据
    return data_list