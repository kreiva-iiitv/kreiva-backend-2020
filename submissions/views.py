from django.shortcuts import render
from submissions.models import *
from submissions.serializers import *
from rest_framework import viewsets


class TeamSubmissionViewSet(viewsets.ModelViewSet):
    queryset = TeamSubmission.objects.all()
    serializer_class = TeamSubmissionSerializer
    http_method_names = ['get', 'post', 'head']


class IndividialPhotoSubmissionViewSet(viewsets.ModelViewSet):
    queryset = IndividialPhotoSubmission.objects.all()
    serializer_class = IndividialPhotoSubmissionSerializer
    http_method_names = ['get', 'post', 'head']


class IndividialVideoSubmissionViewSet(viewsets.ModelViewSet):
    queryset = IndividialVideoSubmission.objects.all()
    serializer_class = IndividialVideoSubmissionSerializer
    http_method_names = ['get', 'post', 'head']

# Create your views here.
