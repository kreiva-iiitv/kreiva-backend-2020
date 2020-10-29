from rest_framework import serializers
from participant.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)


class ParticipantSerializer(serializers.ModelSerializer):

    class Meta:

        model = Participant
        fields = '__all__'
