from django.contrib import admin
from serverview.models import *
from django.http import HttpResponseRedirect
from utils.xlsxlib import writeExcel, writeExcelBig
from wxBotServer.settings import EXCEL_ROOT
import time


@admin.register(ExtensionRegister)
class ExtensionRegisterAdmin(admin.ModelAdmin):
    list_display = ["get_ext_name", "remark", "ext_rank", "is_show", "is_use", 'ext_create_regist']
    list_editable = ["ext_rank", "is_show", "is_use"]


# 导出 excel1 给 CoinRecords(币查询记录) 和 GroupUsers(发消息用户) 用
def output_excel_test(modeladmin, request, queryset):
    filename = "{}.xlsx".format(time.strftime("%Y%m%d%H%M%S"))
    data = []

    for item in queryset:
        data.append({
            "gname": item.from_group,
            "nickname": item.from_user,
            "wxid": item.wxid
        })
    writeExcelBig(EXCEL_ROOT + "/" + filename, data)
    return HttpResponseRedirect("/download?filename={}".format(filename))


# 导出 excel1 给 GroupUsersModel(群员) 用
def output_excel_for_grouusers(modeladmin, request, queryset):
    filename = "{}.xlsx".format(time.strftime("%Y%m%d%H%M%S"))
    data = []

    for item in queryset:
        data.append({
            "gname": item.group.group_name,
            "nickname": item.nickname,
            "wxid": item.wxid
        })
    writeExcelBig(EXCEL_ROOT + "/" + filename, data)
    return HttpResponseRedirect("/download?filename={}".format(filename))


output_excel_for_grouusers.short_description = "导出选中的数据"


@admin.register(CoinRecords)
class CoinRecordsAdmin(admin.ModelAdmin):
    list_display = ["coin_name", "from_user", "wxid", "from_group", "create_time"]
    search_fields = ['coin_name', "from_user"]
    list_filter = ["coin_name"]
    actions = [output_excel_test]


@admin.register(ActiveUsers)
class ActiveUsersAdmin(admin.ModelAdmin):
    list_display = ['from_user', "wxid", 'from_group', 'count', 'create_day_time', 'create_time']
    list_filter = ['create_day_time']
    actions = [output_excel_test]


@admin.register(GroupsModel)
class GroupsModelAdmin(admin.ModelAdmin):
    list_display = ["get_group_name", "group_chatroom", "people_count"]
    search_fields = ["group_name"]


@admin.register(GroupUsersModel)
class GroupUsersModelAdmin(admin.ModelAdmin):

    list_display = ["nickname", "wxid", "group", "create_time"]
    search_fields = ["group__group_name", "group__group_chatroom", "nickname"]
    actions = [output_excel_for_grouusers]

    class Meta:
        css = {
            "all": ("/static/css/zui.min.css", )
        }

        js = (
            "/static/js/jquery.min.js",
            "/static/js/zui.min.js",
        )
