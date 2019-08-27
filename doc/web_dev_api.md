> 此处说明一下服务器提供的一些可能对插件有帮助的api函数

+ `zhcn` 中文处理

<pre>
<code>from utils.core import zhcn
zhcn(name, default="私人消息", error="未获取到")
</code>
</pre>

<table border="0" cellspacing="0">
    <tr>
        <th>参数</th>
        <th style="min-width: 400px;">说明</th>
    </tr>
    <tr>
        <td><em>name</em></td>
        <td>传入要处理的字符串. 如果字符串正常, 则返回转码后的字符串.</td>
    </tr>
    <tr>
        <td><em>default</em></td>
        <td>当name传递为空或者未获取到name的值的时候,返回 <em>default</em> 的值.默认为 <em>私人消息</em></td>
    </tr>
    <tr>
        <td><em>error</em></td>
        <td>当name传递为空白字符串的时候, 返回<em>error</em> 的值.默认为 <em>未获取到</em></td>
    </tr>
</table>

<div style="margin-top: 10px;"></div>
+ `wxResponse` 机器人数据响应封装函数
<pre>
<code>from utils.core import wxResponse
wxResponse(rs=1, tip="贝宝机器人", end=0)
</code>
</pre>

<table border="0" cellspacing="0">
    <tr>
        <th>参数</th>
        <th style="min-width: 400px;">说明</th>
    </tr>
    <tr>
        <td><em>rs</em></td>
        <td>响应状态码.默认为 <em>1</em>.其他状态码参考 <a href="http://www.wqchat.com/apihelp_1.html">HttpApi文档</td>
    </tr>
    <tr>
        <td><em>tip</em></td>
        <td>机器人回复的文本内容.默认为 <em>空</em></td>
    </tr>
    <tr>
        <td><em>end</em></td>
        <td>结束标记.默认为<em>0</em></td>
    </tr>
</table>