from serverview.models import ExtensionRegister
from utils.core import wxResponse


def Extension(request, cotent):
    extensions = ExtensionRegister.objects.filter(is_show=True)

    ret = "功能列表 [备注(正则)]: \n"

    for index, extension in enumerate(extensions):
        ret += "{}({})\n".format(extension.remark, extension.ext_regx)
    return wxResponse(tip=ret)
