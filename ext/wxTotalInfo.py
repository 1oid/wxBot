from serverview.models import GroupUsersModel
from serverview.models import GroupsModel
from serverview.models import CoinRecords
from django.db.models import Count
from utils.core import wxResponse
from datetime import date


def Extension(request, content):
    users = GroupUsersModel.objects.count()
    groups = GroupsModel.objects.count()
    _today = date.today()
    today_search = CoinRecords.objects.filter(create_time__month=_today.month, create_time__day=_today.day)

    max_today_search = today_search.values("coin_name").order_by().annotate(Count("coin_name")).order_by("-coin_name__count")[0]
    # 数据赋值
    ret = ""
    ret += "群员总数: {}\n".format(users)
    ret += "群总数: {}\n".format(groups)
    ret += "今日搜索量: {}\n".format(today_search.count())
    ret += "今日搜索最多: {}\n".format(max_today_search.get("coin_name"))
    ret += "今日搜索最多的数量: {}".format(max_today_search.get("coin_name__count"))

    return wxResponse(tip=ret)
