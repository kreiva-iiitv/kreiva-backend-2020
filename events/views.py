from decimal import ConversionSyntax
from django.shortcuts import render
from rest_framework import response
from events.models import *
from events.serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    http_method_names = ['get',]
    def list(self, request):
        events = []
        for event in self.queryset:
            eventData = self.get_serializer(event)
            responseData = {}
            responseData.update(eventData.data)
            try:
                convener = Member.objects.get(event=event, role='Convener')
                convenerData = MemberSerializer(convener)
                convenerData = convenerData.data
            except Member.DoesNotExist as exp:
                convener = Member(event=event, role='Convener')
                convenerData = MemberSerializer(convener)
                convenerData = convenerData.data

            try:
                co_convener = Member.objects.get(event=event, role='Co-convener')
                co_convenerData = MemberSerializer(co_convener)
                co_convenerData = co_convenerData.data
            except Member.DoesNotExist as exp:
                co_convener = Member(event=event, role='Co-convener')
                co_convenerData = MemberSerializer(co_convener)
                co_convenerData = co_convenerData.data
            
            try:
                committee_coordinator = Member.objects.get(event=event, role='Committee-Coordinator')
                committee_coordinatorData = MemberSerializer(committee_coordinator)
                committee_coordinatorData = committee_coordinatorData.data
            except Member.DoesNotExist as exp:
                committee_coordinator = Member(event=event, role='Committee-Coordinator')
                committee_coordinatorData = MemberSerializer(committee_coordinator)
                committee_coordinatorData = committee_coordinatorData.data
        
            responseData['Convener'] = convenerData
            responseData['coConvener'] = co_convenerData
            responseData['committeeCoordinator'] = committee_coordinatorData
            events.append(responseData)
        return Response({'Events': events}, status=status.HTTP_200_OK)

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    http_method_names = ['get',]
# Create your views here.

class LampStatus(APIView):

    def get(self, request):
        f = open("/home/ubuntu/kreiva-backend-2020/status.txt", "r")
        x = int(f.read())
        f.close()
        return Response({'out':x}, status=status.HTTP_200_OK)

class LampStatusPost(APIView):

    def get(self, request):
        x = request.GET.get('status')
        if x is None:
            x=0
        f = open("/home/ubuntu/kreiva-backend-2020/status.txt", "w")
        f.write(f"{x}")
        f.close()
        return Response({'out':x})
