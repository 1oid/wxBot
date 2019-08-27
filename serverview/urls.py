from django.urls import path
from serverview.views import index, download, initiative
from serverview.views import groupusers, apidoc

urlpatterns = [
    path("", index.Index.as_view()),
    path("download", download.Download.as_view()),
    path("initiative", initiative.Initative.as_view()),
    path("admin/groupuser", groupusers.GroupUsers.as_view()),
    path("apidoc/", apidoc.Index.as_view(), name="apidoc"),
    path("apidoc/<str:doc>", apidoc.Index.as_view(), name="apidoc")
]
