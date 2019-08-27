from django.views.generic import View
from django.http import HttpResponse
from wxBotServer.settings import EXCEL_ROOT
import os


class Download(View):

    def get(self, request):
        filename = request.GET.get("filename", None)

        filename = filename.replace("..", ".")
        if len(filename.split(".")) > 3:
            return HttpResponse("文件不存在")

        if filename and os.path.exists(EXCEL_ROOT + "/" + filename):
            with open(EXCEL_ROOT + "/" + filename, 'rb') as f:
                response = HttpResponse(f.read())
                response["Content-Type"] = "application/octet-stream"
                response['Content-Disposition'] = 'attachment;filename="{}"'.format(filename)
            return response
        return HttpResponse("文件不存在")
