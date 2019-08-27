from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from serverview.models import ExtensionRegister
from utils.core import Extenion
from serverview.models import GroupsModel
import json


class Initative(View):

    def get(self, request):
        return JsonResponse({"code": 1})

    def post(self, request):

        grouplist = request.POST.get("grouplist", None)

        if grouplist:

            if len(grouplist) == GroupsModel.objects.all().count():
                return HttpResponse("")

            grouplist = json.loads(grouplist)
            for group in grouplist:
                username = group.get("username")
                nickname = group.get("nickname")

                if GroupsModel.objects.filter(group_name=nickname, group_chatroom=username).count() == 0:
                    GroupsModel.objects.create(group_chatroom=username, group_name=nickname)
            return HttpResponse("")
        return HttpResponse('{"rs":15,"end":1}')
        # return HttpResponse('{"rs":10,"tip":"这里是返回的内容,可以为空","wxid":"23364342878@chatroom","end":0}')
