from flights.models import AirportsData
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.serializers import Serializer
from flights.models import Flights,AirportsData,Tickets
from .serializer import FlightSerializer,AirportDataSerializer, TicketsSerializer
from rest_framework.views import APIView

class FlightListView(APIView):
    queryset = Flights.objects.all()[:10]
    serializer_class = FlightSerializer

class TicketListView(ListAPIView):
    queryset = Tickets.objects.all()[:7]
    serializer_class = TicketsSerializer


class AirportView(APIView):

    def get(self, request):
        airport_code = request.query_params.get('code',None)
        if 'code' in request.query_params and not len(airport_code):
            return Response({'error_msg': "Please inter airoprt code"})
        if 'code' not in request.query_params:
            queryset = AirportsData.objeects.all()
            res = AirportDataSerializer(queryset, many=True)
            return Response(res.data)
        else:
            queryset= AirportsData.objects.filter(airport_code=airport_code)
            if not queryset:
                return Response({"error_msd": "No airport is found"})
            
            else:
                res = AirportDataSerializer(queryset, many=True)
                return Response(res.data)

    def post(self, request):
        new_data = request.data
        serializer = AirportDataSerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message": "New airport data created"})
        else:
            return Response({"success": False, "massege": "Please provide valid information"})

    
