from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render


class GraphPageView(TemplateView):

    template_name = "graph.html"
