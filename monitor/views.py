from django.http import HttpResponse
from django.views import View
from django.shortcuts import render


class GraphPageView(View):
    def get(self, request):
        return HttpResponse("Hello Alan")
