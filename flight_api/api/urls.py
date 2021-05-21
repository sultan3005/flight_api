from flights.models import Tickets
from django.urls import path
from .views import FlightListView,AirportView,TicketListView
app_name='api'
urlpatterns = [
    path('flights/', FlightListView.as_view(), name='flights'),
    path('airports/', AirportView.as_view(), name='airports'),
    path('tickets/', TicketListView.as_view(), name='tickets'),
]