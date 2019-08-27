from django.views.generic import View
from serverview.models import ActiveUsers, ExtensionRegister, CoinRecords
from django.http import JsonResponse, HttpResponse
from utils.core import Extenion, zhcn
import time
import re
import json


class Index(View):

    # 保存活跃用户
    def active_user_update(self, request):
        nickname = request.POST.get("nickname")
        gname = request.POST.get("gname")
        t = time.strftime("%Y-%m-%d")

        nickname = nickname.encode('utf-8').decode("unicode_escape")
        if gname and "\\u" in gname:
            gname = gname.encode('utf-8').decode("unicode_escape")
        else:
            gname = "未获取到群名"
        wxid = request.POST.get("mid", "未获取到")

        # 对应的群中用户不存在, 数据库中创建一个
        if ActiveUsers.objects.filter(from_user=nickname, from_group=gname, create_day_time=t).count() == 0:
            ActiveUsers.objects.create(from_user=nickname, from_group=gname, create_day_time=t, wxid=wxid)
        user = ActiveUsers.objects.get(from_user=nickname, from_group=gname, create_day_time=t)
        user.count += 1
        user.wxid = wxid
        user.save()

    # 发来的消息编码
    def encoder(self, content):
        if '\\u' in content:
            return content.encode('utf-8').decode("unicode_escape")
        return content

    def get(self, request):
        return JsonResponse({"rs": 1})

    def post(self, request):
        content = request.POST.get("content", "")

        # 减小服务器压力, 消息长度不得超过15
        if len(self.encoder(content)) > 15:
            return HttpResponse("")

        # 记录活跃用户
        self.active_user_update(request)

        # 获取所有插件
        extension_registers = ExtensionRegister.objects.filter(is_use=True).order_by("-ext_rank")
        # 循环已存在的插件
        for extension_register in extension_registers:

            # 如果正则匹配, 则调用对应插件
            if re.match(extension_register.ext_regx, self.encoder(content)):

                extension = Extenion().load_extension(extension_register.ext_file.name)

                # 如果插件存在，调用插件
                if extension:
                    text = extension.Extension(request, content)
                    if text:
                        return HttpResponse(text)
        return HttpResponse('')

