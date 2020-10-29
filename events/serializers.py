from rest_framework import serializers
from events.models import *


class EventSerializer(serializers.ModelSerializer):

    class Meta:

        model = Event
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):

    #team = serializers.ReadOnlyField(source='Team')
    class Meta:

        model = Member
        fields = '__all__'
