import sys
from config import logger, EXTENSIONS_PATH
import os
from wxBotServer.settings import BASE_DIR
import json


class Extenion(object):

    def __init__(self):
        self.syspath = BASE_DIR + "/" + EXTENSIONS_PATH

        self.start()

    def init_path(self):
        '''
        初始化插件路径
        :return:
        '''
        sys.path.append(self.syspath)

    # 加载插件
    def load_extension(self, ext_name):
        ext_name = ext_name.replace(EXTENSIONS_PATH, "").replace("/", "")

        if len(ext_name.split(".")) == 2 and ext_name.split(".")[1] == "py":
            ext_name = ext_name.split(".")[0]
        else:
            return False

        try:
            md = __import__(ext_name)
            print(dir(md))
            return md
        except ModuleNotFoundError as e:
            logger.info("{} illegal...{}.".format(ext_name, e))
            return False

    # 列插件
    @staticmethod
    def list_extentions():
        exts = [x for x in os.listdir(BASE_DIR + "/" + EXTENSIONS_PATH) if x[:8] != '__init__' and x[-2:] == "py"]
        return exts

    def start(self):
        self.init_path()


# 中文处理
def zhcn(name, default="私人消息", error="未获取到"):
    if not name:
        return default
    else:
        if name and "\\u" in name:
            name = name.encode('utf-8').decode("unicode_escape")
        elif name == "":
            name = error
    return name


# 封装适合接口的响应函数
def wxResponse(rs=1, tip="", end=0):
    ret = {
        "rs": rs,
        "tip": tip,
        "end": end
    }
    return json.dumps(ret).replace(", ", ",").replace(": ", ":").encode("utf-8").decode("unicode_escape")

