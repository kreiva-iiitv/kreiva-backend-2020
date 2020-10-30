from rest_framework import serializers
from teams.models import *


class TeamSerializer(serializers.ModelSerializer):

    class Meta:

        model = Team
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):

    team =TeamSerializer(read_only=True)

    class Meta:

        model = Member
        fields = '__all__'
