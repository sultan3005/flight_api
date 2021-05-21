from django.urls import path
from .views import FlightListView,AirportView
app_name='api'
urlpatterns = [
    path('flights/', FlightListView.as_view(), name='flights'),
    path('airports/', AirportView.as_view(), name='airports')
]