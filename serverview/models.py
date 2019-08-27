from django.db import models
from django.utils.html import format_html
import os


class ExtensionRegister(models.Model):
    ext_regx = models.CharField(max_length=100, verbose_name="触发匹配")
    remark = models.CharField(max_length=100, verbose_name="备注", blank=True, default="")
    ext_create_regist = models.DateTimeField(auto_now_add=True, verbose_name="插件注册时间")
    # is_initiative = models.BooleanField(verbose_name="是否主动接口", default=False)
    ext_file = models.FileField(upload_to='.', verbose_name="插件文件", blank=True)
    ext_rank = models.IntegerField(default=0, blank=True, verbose_name="优先级", help_text="整型, 防止某些插件规则冲突")

    is_show = models.BooleanField(default=True, blank=True, verbose_name="是否在功能列表中显示")
    is_use = models.BooleanField(default=True, blank=True, verbose_name="启用/停用")

    def __str__(self):
        return self.ext_file.name

    def get_ext_name(self):
        return os.path.split(self.ext_file.name)[-1]

    get_ext_name.short_description = "插件名"

    class Meta:
        verbose_name_plural = "插件注册"
        ordering = ["-ext_rank"]


# 货币记录
class CoinRecords(models.Model):
    coin_name = models.CharField(max_length=20, verbose_name="货币名称")
    from_user = models.CharField(max_length=50, verbose_name="来源用户")
    from_group = models.CharField(max_length=50, verbose_name="来源群组")
    create_time = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="创建时间")
    wxid = models.CharField(max_length=100, verbose_name="微信id", default="空", blank=True)

    def __str__(self):
        return self.from_user

    class Meta:
        verbose_name_plural = "查询记录"
        ordering = ["-create_time"]


# 记录活跃用户
class ActiveUsers(models.Model):
    from_user = models.CharField(max_length=50, verbose_name="来源用户")
    from_group = models.CharField(max_length=50, verbose_name="来源群组")
    create_time = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="创建时间")
    create_day_time = models.CharField(max_length=50, verbose_name="创建时间分类记录", blank=True, default="2019-01-01")
    count = models.IntegerField(default=0, blank=True, verbose_name="发言次数")
    wxid = models.CharField(max_length=100, verbose_name="微信id", default="空", blank=True)

    def __str__(self):
        return self.from_user

    class Meta:
        verbose_name_plural = "活跃记录"
        ordering = ['-create_day_time', '-count']


# 群组
class GroupsModel(models.Model):
    group_name = models.CharField(max_length=100, verbose_name="群组名称")
    group_chatroom = models.CharField(max_length=100, verbose_name="群组id")

    def __str__(self):
        return self.group_name

    def get_group_name(self):
        if self.group_name:
            return format_html("<a href='/admin/serverview/groupusersmodel/?q={group_chatroom}'>"
                               "{group_name}</a>".format(group_chatroom=self.group_chatroom, group_name=self.group_name))
        return self.group_name

    def people_count(self):
        return self.groupusersmodel_set.count()

    class Meta:
        verbose_name_plural = "所有群"

    people_count.short_description = "群员人数"
    get_group_name.short_description = "群名称"


# 群用户
class GroupUsersModel(models.Model):
    group = models.ForeignKey(GroupsModel, on_delete=models.CASCADE, verbose_name="群组")
    wxid = models.CharField(max_length=100, verbose_name="wxid")
    nickname = models.CharField(max_length=100, verbose_name="微信名")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name_plural = "所有群成员"

