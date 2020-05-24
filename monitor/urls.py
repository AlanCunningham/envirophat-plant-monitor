from django.urls import path
from monitor.views import GraphPageView, SensorDataHistoryView, SensorDataCurrentView

urlpatterns = [
    path("graph/", GraphPageView.as_view()),
    path("sensor_data_history/", SensorDataHistoryView.as_view()),
    path("sensor_data_current/", SensorDataCurrentView.as_view()),
]
