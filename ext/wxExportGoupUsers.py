from serverview.models import GroupUsersModel
from wxBotServer.settings import EXCEL_ROOT
from utils.xlsxlib import writeExcelBig
from utils.core import wxResponse
import time


def Extension(request, contnet):
    users = GroupUsersModel.objects.all()
    filename = "export_{}.xlsx".format(time.strftime("%Y%m%d%H%M%S"))

    data = []
    for user in users:
        d = {
            "gname": user.group.group_name,
            "nickname": user.nickname,
            "wxid": user.wxid
        }
        data.append(d)
    writeExcelBig(EXCEL_ROOT + "/" + filename, data)
    return wxResponse(tip="http://{}/download?filename={}".format(request.META['HTTP_HOST'], filename))
