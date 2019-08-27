import logging
from wxBotServer.settings import BASE_DIR
import os

'''
logging 配置
'''
LOGGING_FILENAME = "data/logs.log"
LOGGING_FILEMODE = "w"
LOGGING_FORMAT = "[%(levelname)s][%(asctime)s] %(message)s"
LOGGING_DATE_FORMAT = "%d-%M-%Y %H:%M:%S"
LOGGING_LEVEL = logging.INFO
logging.basicConfig(format=LOGGING_FORMAT, datefmt=LOGGING_DATE_FORMAT, level=LOGGING_LEVEL)
logger = logging

'''
爬虫配置
THREAD: 多线程并发数
WORK_SLEEP: 任务间隔时间
DEFAULT_PAGE: 默认爬行页数
'''
THREAD = 5
WORK_SLEEP = 30
DEFAULT_PAGE = 31
DATA_JSON_SAVE = "data/data.json"


'''
插件配置
插件路径
插件注册, 插件白名单，防止无用插件调用
'''
EXTENSIONS_PATH = 'ext'
