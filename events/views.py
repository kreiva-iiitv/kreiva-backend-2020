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
                member = Member.objects.get(event=event, role='Member')
                memberData = MemberSerializer(member)
                memberData = memberData.data
            except Member.DoesNotExist as exp:
                member = Member(event=event, role='Member')
                memberData = MemberSerializer(member)
                memberData = memberData.data
        
            responseData['Convener'] = convenerData
            responseData['Co-Convener'] = co_convenerData
            responseData['Member'] = memberData
            events.append(responseData)
        return Response({'Events': events}, status=status.HTTP_200_OK)

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

# Create your views here.
