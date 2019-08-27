from django.shortcuts import render
from django.views.generic import View
from wxBotServer.settings import BASE_DIR
from markdown import markdown
import os
import json


class Index(View):

    doc_path = os.path.join(BASE_DIR, "doc")

    # 加载 apidocs
    def load_api_docs(self):
        with open(self.doc_path + "/list.json", encoding="utf-8") as f:
            data = json.load(f)
        return data

    # # 将数据格式化成新的序列
    # def data_to_list(self, data):
    #     for item in data:
    #         pass
    # 制定文档读取
    def get_doc(self, path):
        filename = "{}/{}.md".format(self.doc_path, path)
        if os.path.exists(filename):
            with open(filename, encoding="utf-8") as f:
                data = f.read()
            return data
        return None

    # 把数据转换为 dict
    def data_to_dict(self, data):
        ret = {}

        for item in data:
            title, path = item.get("title"), item.get("path")

            ret[path] = {
                "title": title,
                "path": path
            }
        return ret

    def get(self, request, doc=None):
        data = self.load_api_docs()

        # 数据变为 json 方便取数据
        json_data = self.data_to_dict(data)

        if not doc:
            doc = data[0].get("path")

        # 判断数据是否存在
        if json_data.get(doc, None):
            title = json_data.get(doc).get("title")
            article = markdown(self.get_doc(path=doc))
        else:
            title = "贝宝机器人"
            article = "贝宝机器人"

        return render(request, "api.html", {"nav_list": data, "info": {
                "title": title,
                "article": article,
                "path": ""
            }})
