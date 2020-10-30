from django.shortcuts import render
from participant.models import *
from participant.serializers import *
from rest_framework import viewsets
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

# Create your views here.
class GoogleView(APIView):

    def post(self, request):
        payload = {'access_token': request.data.get("token")}  # validate the token
        r = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', params=payload)
        data = json.loads(r.text)
        #return Response(data)

        if 'error' in data:
            content = {'message': 'wrong google token / this google token is already expired.'}
            return Response(content)
        # create user if not exist
        #print(data)
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            user = User()
            user.username = data['email']
            # provider random default password
            user.password = make_password(BaseUserManager().make_random_password())
            user.email = data['email']
            user.first_name = data['given_name']
            user.last_name = data['family_name']
            user.save()

        token = RefreshToken.for_user(user)  # generate token without username & password
        response = {}
        response['name'] = data['name']
        response['email'] = user.email
        response['picture'] = data['picture']
        response['access_token'] = str(token.access_token)
        response['refresh_token'] = str(token)
        return Response(response)
