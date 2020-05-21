from django.urls import path
from monitor.views import GraphPageView, SensorDataView

urlpatterns = [
    path('graph/', GraphPageView.as_view()),
    path('sensordata/', SensorDataView.as_view()),
]