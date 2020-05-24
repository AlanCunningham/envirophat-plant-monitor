from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from django.utils.timezone import now
from datetime import timedelta
from monitor.models import SensorData
from . import sensor_helper


class GraphPageView(TemplateView):

    template_name = "graph.html"


class SensorDataHistoryView(TemplateView):
    """
    Get a historical view of sensor data from the SensorData model.
    """

    model = SensorData

    def get(self, *args, **kwargs):
        sensor_data = SensorData.objects.filter(
            datetime__gte=now()-timedelta(days=3)
        ).values()
        for item in sensor_data:
            item["datetime"] = item["datetime"].strftime("%a %d %H:%M")
        return JsonResponse({"sensor_data": list(sensor_data)})


class SensorDataCurrentView(TemplateView):
    """
    Get the current sensor readings.
    """

    def get(self, *args, **kwargs):
        sensor_data = sensor_helper.get_sensor_data()
        return JsonResponse(sensor_data)