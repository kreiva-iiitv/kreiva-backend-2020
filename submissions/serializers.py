from rest_framework import serializers
from submissions.models import *


class TeamSubmissionSerializer(serializers.ModelSerializer):

    class Meta:

        model = TeamSubmission
        fields = '__all__'


class IndividialPhotoSubmissionSerializer(serializers.ModelSerializer):

    #team = serializers.ReadOnlyField(source='Team')
    class Meta:

        model = IndividialPhotoSubmission
        fields = '__all__'


class IndividialVideoSubmissionSerializer(serializers.ModelSerializer):

    class Meta:

        model = IndividialVideoSubmission
        fields = '__all__'
