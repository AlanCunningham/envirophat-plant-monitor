from django.urls import path
from monitor.views import GraphPageView

urlpatterns = [
    path('graph/', GraphPageView.as_view()),
]