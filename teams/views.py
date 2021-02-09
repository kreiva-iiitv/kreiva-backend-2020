from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from teams.models import *
from teams.serializers import *
from teams.forms import *
from rest_framework import viewsets, status



class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    http_method_names = ['get', ]
    def list(self, request):
        teams = self.get_serializer(self.queryset, many=True)
        return Response({'Team': teams.data}, status=status.HTTP_200_OK)


class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    http_method_names = ['get', ]
