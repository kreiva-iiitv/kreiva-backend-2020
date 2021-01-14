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

    def list(self, request):
        teams = []
        for team in self.queryset:
            teamData = self.get_serializer(team)
            resppnseData = {}
            resppnseData.update(teamData.data)

            member = TeamMember.objects.filter(team=team).order_by('-rolepriority')
            if len(member) == 0:
                member = TeamMember(team=team)
            memberData = TeamMemberSerializer(member, many=True)
            resppnseData['teamMembers'] = memberData.data
            teams.append(resppnseData)
        return Response({'Team': teams}, status=status.HTTP_200_OK)            



class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
