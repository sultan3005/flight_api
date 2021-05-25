from django.http import request
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.serializers import Serializer
from flights.models import Flights,AirportsData,Tickets
from .serializer import FlightSerializer,AirportDataSerializer, TicketsSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

class FlightListView(APIView):
    queryset = Flights.objects.all()[:10]
    serializer_class = FlightSerializer

class TicketListView(ListAPIView):
    queryset = Tickets.objects.all()[:7]
    serializer_class = TicketsSerializer


class AirportView(APIView):
    authentication_classes = (BasicAuthentication,)
    permissions_classes = (IsAuthenticated,)

    def get(self, request):
        airport_code = request.query_params.get('code',None)
        if 'code' in request.query_params and not len(airport_code):
            return Response({'error_msg': "Please inter airoprt code"})
        if 'code' not in request.query_params:
            queryset = AirportsData.objects.all()
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
    def delete(self, request):
        airport_code = request.query_params.get('code')
        snippet = self.get_object(airport_code)
        snippet.delete()
        return Response({'success':True, 'message': 'Airport deleted from DB'})
        #delete airport by code
        


    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update():
        #update airport by code
        if kwargs.__len__() !=0:
            tableid = kwargs['id']
            mycol = request.DATA['col']
            AirportsData.objects.filter(id=tableid).update(col=mycol)

        pass 
    
    #В serializers по аэропорту вытащить все полеты аэропорта 
    #Прочитать про authentication 
    
