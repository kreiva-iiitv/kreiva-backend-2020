from rest_framework import serializers
from teams.models import *

class TeamMemberSerializer(serializers.ModelSerializer):

    class Meta:

        model = TeamMember
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    teamMembers = serializers.SerializerMethodField()
    
    class Meta:

        model = Team
        fields = '__all__'

    def get_teamMembers(self, instance):
        teamMembers = instance.teamMembers.all().order_by('rolepriority')
        return TeamMemberSerializer(teamMembers, many=True, context={"request": self.context.get('request')}).data
