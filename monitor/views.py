from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from django.utils.timezone import now
from datetime import timedelta
from monitor.models import SensorData


class GraphPageView(TemplateView):

    template_name = "graph.html"


class SensorDataView(TemplateView):

    model = SensorData

    def get(self, *args, **kwargs):
        sensor_data = SensorData.objects.filter(
            datetime__gte=now()-timedelta(days=2)
        ).values()
        for item in sensor_data:
            item["datetime"] = item["datetime"].strftime("%a %d %H:%M")
        return JsonResponse({"sensor_data": list(sensor_data)})