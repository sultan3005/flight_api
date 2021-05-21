from rest_framework import serializers
from flights.models import Flights, Tickets, AirportsData

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flights
        fields = [ 'flight_no', 'scheduled_departure', 'scheduled_arrival', 'departure_airport',
                  'arrival_airport', 'status']

class AirportDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirportsData
        fields = ['airport_code', 'airport_name', 'city', 'coordinates', 'timezone']

class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = ['ticket_no',  'passenger_id', 'passenger_name', ]             

