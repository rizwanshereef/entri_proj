from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CandidateSerializer, InterviewerSerializer
from .models import Candidate, Interviewer
from datetime import datetime
from datetime import date as dt

# View for Candidate serializer
class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all().order_by('name')
    serializer_class = CandidateSerializer

    def perform_create(self, serializer):
        serializer.save()

# View for Interviewer Serializer
class InterviewerViewSet(viewsets.ModelViewSet):
    queryset = Interviewer.objects.all().order_by('name')
    serializer_class = InterviewerSerializer

    def perform_create(self, serializer):
        serializer.save()

# View for HR api
class HRView(APIView):

    def post(self, request, format = None):
        
        #reponse value initialize
        idate = None
        slot_start_time = None
        slot_end_time = None
        candidate_id = None
        candidate_name = ""
        interviewer_id = None
        interviewer_name = ""
        message = ""

#store post values from the API
        can_id = request.data['can_id']
        int_id = request.data['int_id']
        
#Exception handling if the entered values are incorrect
        try:
            candidate = Candidate.objects.get(candidate_id=can_id)
        except Exception:
            message = "Invalid Candidate ID"
            return Response({'message':message})
        try:
            interviewer =Interviewer.objects.get(interviewer_id=int_id)
        except Exception:
            message = "Invalid Interviewer ID"
            return Response({'message':message})
        

# Assign model values to variables for computation
        candidate_name= candidate.name
        candidate_date = candidate.date
        candidate_from = candidate.start_time
        candidate_to = candidate.end_time

        interviewer_name = interviewer.name
        interviewer_date = interviewer.date
        interviewer_from = interviewer.start_time
        interviewer_to = interviewer.end_time

#Condition to check whether the dates are same  
        if(candidate_date == interviewer_date):
            idate= candidate.date # storing date for Response
# time comparison for finding slots.
            if candidate_from < interviewer_from and candidate_to < interviewer_from:
                message = "No slot available"

            elif interviewer_from < candidate_from and interviewer_to < candidate_from:
                message = "No slot available"

            else:
                slot_start_time = max([candidate_from, interviewer_from])
                slot_end_time = min([candidate_to, interviewer_to])

# type cast datetime.date() to datetime.datetime 
                slot_end = datetime.combine(dt.today(), slot_end_time) 
                slot_start = datetime.combine(dt.today(), slot_start_time)

#Check if slots satisfies the 1 hour slot duration 
                if slot_start and slot_end: 
                    if  (slot_end - slot_start).seconds < 3600:
                        message = "No slot available"
                    else:
                    
                        message = "Slot Available"
        else:
            message = "Date Mismatch, No slot available"
        
# Response message to show the computed available slots
        
        return Response(
            {
                'message' : message,
                'date' : idate,
                'candidate ID': can_id,
                'Candidate Name': candidate_name,
                'Interviewer ID': int_id,
                'Interviewer Name': interviewer_name,
                'slot_start_time' : slot_start_time,
                'slot_end_time' : slot_end_time
            }
        )      