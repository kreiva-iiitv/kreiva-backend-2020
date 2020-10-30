from django.shortcuts import render
from submissions.models import *
from submissions.serializers import *
from rest_framework import viewsets


class TeamSubmissionViewSet(viewsets.ModelViewSet):
    queryset = TeamSubmission.objects.all()
    serializer_class = TeamSubmissionSerializer


class IndividialPhotoSubmissionViewSet(viewsets.ModelViewSet):
    queryset = IndividialPhotoSubmission.objects.all()
    serializer_class = IndividialPhotoSubmissionSerializer


class IndividialVideoSubmissionViewSet(viewsets.ModelViewSet):
    queryset = IndividialVideoSubmission.objects.all()
    serializer_class = IndividialVideoSubmissionSerializer

    

# Create your views here.
