from rest_framework import serializers
from submissions.models import *
from participant.serializers import ParticipantSerializer
from events.serializers import EventSerializer


class TeamSubmissionSerializer(serializers.ModelSerializer):

    #participant = ParticipantSerializer(read_only=True)
    #event = EventSerializer(read_only=True)
    class Meta:

        model = TeamSubmission
        fields = '__all__'


class IndividialPhotoSubmissionSerializer(serializers.ModelSerializer):

    #participant = ParticipantSerializer(read_only=True)
    #event = EventSerializer(read_only=True)
    class Meta:

        model = IndividialPhotoSubmission
        fields = ('participant', 'event', 'photo')


class IndividialVideoSubmissionSerializer(serializers.ModelSerializer):

    #participant = ParticipantSerializer(read_only=True)
    #event = EventSerializer(read_only=True)
    class Meta:

        model = IndividialVideoSubmission
        fields = '__all__'
