from rest_framework import serializers
from events.models import *

class MemberSerializer(serializers.ModelSerializer):

    class Meta:

        model = Member
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):

    eventmember = MemberSerializer(many=True) 

    class Meta:

        model = Event
        fields = '__all__'

    def create(self, validated_data):
        eventmemberValidated = validated_data.pop('eventmember')
        event = Event.objects.create(**validated_data)
        for member in eventmemberValidated:
            Member.objects.create(event=event, **member)
        return event 
