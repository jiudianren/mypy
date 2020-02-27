# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/8/21 15:58

from functools import wraps
import traceback
import logging


def pylearnlog( log_level=logging.DEBUG, name="default_name"):
    # log实例
    logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    re = logging.getLogger(name)
    # 创建handler 写到控制台，或者日志文件等
    hds = logging.StreamHandler()
    #fds = logging.FileHandler("C://Users//10259187//Desktop//Test//log.txt",mode='w', encoding='utf-8')
    # 给实例增加处理方式
    re.addHandler(hds)
    # 设置日志级别
    # logger.setLevel(logging.WARN)
    re.setLevel(log_level)
    return re


logger = pylearnlog()


def start_log(func):
    @wraps(func)
    def logs(*args, **kwargs):
        try:
            #logger.debug("FUNC START:{0}".format(func.__name__))
            logger.debug(f"FUNC START:{func.__name__}")
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"{func.__name__} is error,here are details:\n {traceback.format_exc()}")
    return logs


@start_log
def test_log_start(para):
    print("test:{0}".format(para))

if __name__ == "__main__":
    test_log_start("para1")