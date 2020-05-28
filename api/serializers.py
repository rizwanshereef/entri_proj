from rest_framework import serializers
from .models import Candidate, Interviewer

#serializer for candidate
class CandidateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidate
        fields= ['candidate_id','name','email_address','phone','date','start_time','end_time']

#serializer for Interviewer
class InterviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interviewer
        fields = ['interviewer_id','name','date','start_time','end_time']

