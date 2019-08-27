+ 环境要求
    - `Python3.7及以上`
    - 其他依赖环境

+ 开发规范
    - 文件命名以大(小)驼峰命名
    - 每个插件的入口函数为 `Extension(request, content)`


+ 插件入口函数 `Extension(request, content)` 说明

<table border="0" cellspacing="0">
    <tr>
        <th>参数</th>
        <th style="min-width: 400px;">说明</th>
    </tr>
    <tr>
        <td><em>request</em></td>
        <td>Django传递过来的值, 里面包含所有的数据信息, 根据需要获得. 例: <em>request.POST.get('nickname')</em></td>
    </tr>
    <tr>
        <td><em>content</em></td>
        <td>用户发送的信息,并且经过转码后的传递.如果要获取原始信息, 可以通过 <em>request.POST.get("content")</em>获取</td>
    </tr>
</table>


+ 插件实例:

<pre>
<code class="hljs cs">
import time
import json
from config import DATA_JSON_SAVE
from wxBotServer.settings import BASE_DIR
from serverview.models import CoinRecords
from utils.core import zhcn
from utils.core import wxResponse


# 数据转换, 人民币-->美元
def PriceConvert(price):
    .....

def Extension(request, content):
    # 加载数据文件
    with open('/'.join([BASE_DIR, DATA_JSON_SAVE])) as f:
        data = json.load(f)
    # 获取所有币的名字
    coinKeys = list(data.keys())

    # 判断币是否在列表里面
    if content.strip().upper() in coinKeys:
        # 保存查询者的数据
        search_user_save(request, content)

        # 查询到币的数据
        coin_item = data.get(content.strip().upper())
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
</code>
</pre>


+ 上传注册插件
    - 登陆 `web` 后台, 系统相关->插件注册->添加插件注册
    - `触发匹配`, 填写触发的正则内容. 为了减少服务器压力, 最大长度为15.
    - `备注`, 方便查看/修改插件.
    - `插件文件`, 将编写好的插件脚本上传.
    - `优先级`, 避免有重叠的正则规则.

![](/static/images/wxbot_extension_1.png)

    