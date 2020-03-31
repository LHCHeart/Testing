import logging
import configparser


# 读取配置文件
conf = configparser.ConfigParser()
conf.read("./conf/test.conf",encoding='UTF-8')

LOG_FILE = conf.get("LOG", "LOG_FILE")
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"    # 日志格式化输出
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"                           # 日期格式
fp = logging.FileHandler(LOG_FILE, encoding='utf-8')        # 日志输出文件
# fp = logging.FileHandler('./logs/running.log', encoding='utf-8')

fs = logging.StreamHandler()
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT, handlers=[fp, fs])

# debug/info/warning/error/critical

def write_debug(debug):
    logging.debug(debug)


def write_info(info):
    logging.info(info)


def write_warning(warning):
    logging.info(warning)


def write_error(error):
    logging.error(error)


def write_critical(critical):
    logging.info(critical)
