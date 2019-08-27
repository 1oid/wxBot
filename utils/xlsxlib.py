from xlrd import open_workbook, biffh
from xlutils.copy import copy
import xlwt
import os


def writeExcel(filename, value_item):
    try:
        book = open_workbook(filename)
        excel = copy(book)
        sheet = book.sheet_by_index(0)

        table = excel.get_sheet(0)
        rows = sheet.nrows

        table.write(rows, 0, value_item.get("gname"))
        table.write(rows, 1, value_item.get("nickname"))
        table.write(rows, 2, value_item.get("wxid"))

        excel.save(filename)
    except FileNotFoundError as e:
        book = xlwt.Workbook()
        sheet = book.add_sheet("1")
        for index, value in enumerate(["群名称", "微信昵称", "微信id"]):
            sheet.write(0, index, value)
        book.save(filename)
        writeExcel(filename, value_item)


# 数据量非常多的时候使用这种方式
def writeExcelBig(filename, value_items):
    try:
        book = open_workbook(filename)
        excel = copy(book)
        sheet = book.sheet_by_index(0)

        table = excel.get_sheet(0)
        rows = sheet.nrows
        print(rows)

        for index, value_item in enumerate(value_items):
            table.write(index+1, 0, value_item.get("gname"))
            table.write(index+1, 1, value_item.get("nickname"))
            table.write(index+1, 2, value_item.get("wxid"))

        excel.save(filename)
    except FileNotFoundError as e:
        book = xlwt.Workbook()
        sheet = book.add_sheet("1")
        for index, value in enumerate(["群名称", "微信昵称", "微信id"]):
            sheet.write(0, index, value)
        book.save(filename)
        writeExcelBig(filename, value_items)

# writeExcel("file.xlsx", {"gname": "wxgroup", "nickname": "wxname", "wxid": "wxid"})

# writeExcel("test2.xlsx", ["测试"])
# def writeAll(filename, retList):
#     for item in retList:
#

# sortedExcel("../doc/www_0898aaa_com-小说书城 03-28.xlsx")

