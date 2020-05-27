from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CandidateSerializer, InterviewerSerializer
from .models import Candidate, Interviewer


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all().order_by('name')
    serializer_class = CandidateSerializer

    def perform_create(self, serializer):
        serializer.save()


class InterviewerViewSet(viewsets.ModelViewSet):
    queryset = Interviewer.objects.all().order_by('name')
    serializer_class = InterviewerSerializer

    def perform_create(self, serializer):
        serializer.save()
        
        