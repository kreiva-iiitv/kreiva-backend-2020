from rest_framework import serializers
from participant.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ('first_name', 'last_name', 'email',)


class ParticipantSerializer(serializers.ModelSerializer):

    user =UserSerializer(read_only=True)

    class Meta:

        model = Participant
        fields = '__all__'
