from rest_framework import serializers
from events.models import *

class MemberSerializer(serializers.ModelSerializer):

    class Meta:

        model = Member
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):

    class Meta:

        model = Event
        fields = '__all__'