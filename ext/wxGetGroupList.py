import json
from utils.core import wxResponse
from serverview.models import GroupsModel, GroupUsersModel


def Extension(request, content):
    gusername = request.POST.get("gusername")

    memberlist = request.POST.get("memberlist", None)

    if memberlist:
        for member in json.loads(memberlist):
            wxid = member.get("username")
            nickname = member.get("nickname")
            # print(member)
            # print(GroupsModel.objects.filter(group_chatroom=gusername).count())

            # 判断群组是否在数据库中, 不在的话 不进行插入
            if GroupsModel.objects.filter(group_chatroom=gusername).count() != 0:
                group = GroupsModel.objects.get(group_chatroom=gusername)

                # 用户不存在的时候插入
                if GroupUsersModel.objects.filter(wxid=wxid, group_id=group.id).count() == 0:
                    GroupUsersModel.objects.create(group_id=group.id, wxid=wxid, nickname=nickname)

        return "ok"
    return wxResponse(rs=10)
