from decimal import ConversionSyntax
from django.shortcuts import render
from rest_framework import response
from events.models import *
from events.serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def list(self, request):
        events = []
        for event in self.queryset:
            eventData = self.serializer_class(event)
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
            responseData['Co-Convener'] = co_convenerData
            responseData['Committee-Coordinator'] = committee_coordinatorData
            events.append(responseData)
        return Response({'Events': events}, status=status.HTTP_200_OK)

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

# Create your views here.
