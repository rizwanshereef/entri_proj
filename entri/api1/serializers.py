from rest_framework import serializers
from .models import Candidate, Interviewer

#serializer for candidate
class CandidateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidate
        fields= ['id','name','email_address','phone','date','start_time','end_time']

#serializer for Interviewer
class InterviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interviewer
        fields = ['id','name','date','start_time','end_time']