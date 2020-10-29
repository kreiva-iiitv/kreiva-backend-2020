from django.shortcuts import render
from events.models import *
from events.serializers import *
from rest_framework import viewsets


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

# Create your views here.
