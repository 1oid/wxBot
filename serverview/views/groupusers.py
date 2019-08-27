from django.views.generic import View
from django.shortcuts import render


class GroupUsers(View):

    def get(self, request):
        return render(request, "some.html")
