'''
POST DATA
{'robotid': ['wxid_gytwlo6oc6d122'], 'skw': ['17348'],
'u': ['105830'], 'isadmin': ['0'], 'nickname': ['Loid'],
'voltype': ['xiaowing3'], 'gadmin': [',,'],
'gname': ['\\u7FA4\\u672A\\u547D\\u540D'],
'robotnickname': ['\\u6D4B\\u8BD5'], a
'msgid': ['1669868689'], 'msgtype': ['1'],
'mid': ['wxid_0tgw07c8w9w222'], 'atlist': [''],
'content': ['cc'], 'vol': ['3.29'], 'username': ['wxid_0tgw07c8w9w222'],
'gid': ['365960'], 'gusername': ['9349219741@chatroom'], 'displayname': ['Loid']}
'''
import time
import json
from config import DATA_JSON_SAVE
from wxBotServer.settings import BASE_DIR
from serverview.models import CoinRecords
from utils.core import zhcn
from utils.core import wxResponse


# 十亿以上显示  XX亿  1<10亿 显示 X.XX亿
# 百万和千万的 显示 XXXX万  XXX万
# 低于百万的正常显示
def PriceConvert(price):
    integer_price = str(int(price))

    if len(integer_price) > 9:
        return integer_price[:len(integer_price) - 8] + "亿"
    elif len(integer_price) > 8:
        return "{}.{}亿".format(integer_price[:len(integer_price) - 8], integer_price[-8:-6])
    elif len(integer_price) > 6:
        return "{}万".format(integer_price[:-4])
    else:
        return price

# 1594358,882461
# PriceConvert(882461)


# 保存查询记录
def search_user_save(request, content):
    if content:
        # 查询记录保存
        nickname = request.POST.get("nickname")
        gname = request.POST.get("gname", None)
        wxid = request.POST.get("mid", "未获取到")

        CoinRecords.objects.create(coin_name=content.strip().upper(),
                                   from_user=zhcn(nickname),
                                   from_group=zhcn(gname),
                                   wxid=wxid)


def Extension(request, coin):
    # 加载数据文件
    with open('/'.join([BASE_DIR, DATA_JSON_SAVE])) as f:
        data = json.load(f)
    # 获取所有币的名字
    coinKeys = list(data.keys())

    # 判断币是否在列表里面
    if coin.strip().upper() in coinKeys:
        # 保存查询者的数据
        search_user_save(request, coin)

        # 查询到币的数据
        coin_item = data.get(coin.strip().upper())
        full_name = coin_item.get("fullname")

        current_price = PriceConvert(round(float(coin_item.get("current_price")) * 0.1457, 2))
        market_value = PriceConvert(round(float(coin_item.get("market_value")) * 0.1457, 2))
        vol = PriceConvert(round(float(coin_item.get("vol")) * 0.1457, 2))

        price = "当前价格: ${}".format(current_price)
        percent = "涨幅: {}%".format(coin_item.get("change_percent"))
        market = "流通市值: ${}".format(market_value)
        vol_24 = "24h成交: {}".format(vol)
        t = "时间: {}".format(time.strftime("%Y-%m-%d %H:%M:%S"))

        # 返回数据给机器人
        return wxResponse(tip="\n".join([full_name, price, percent, market, vol_24, t]))

