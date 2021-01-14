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

            MemberDatas = []
            members = TeamMember.objects.filter(team=team).order_by('-rolepriority')
            for member in members:
                memberData = TeamMemberSerializer(member)
                MemberDatas.append(memberData.data)
            resppnseData['teamMembers'] = MemberDatas
            teams.append(resppnseData)
        return Response({'Team': teams}, status=status.HTTP_200_OK)            



class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
