from rest_framework import serializers
from teams.models import *


class TeamSerializer(serializers.ModelSerializer):

    class Meta:

        model = Team
        fields = '__all__'


class TeamMemberSerializer(serializers.ModelSerializer):

    class Meta:

        model = TeamMember
        fields = '__all__'
