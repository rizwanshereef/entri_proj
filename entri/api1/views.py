from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CandidateSerializer, InterviewerSerializer
from .models import Candidate, Interviewer
from datetime import datetime
from datetime import date as dt

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

        #get post values from the API
        can_id = request.data['can_id']
        int_id = request.data['int_id']
        
        #Exception handling if the entered values are incorrect
        try:
            candidate = Candidate.objects.get(id=can_id)
            print(candidate.date, type(candidate))
        except Exception:
            message = "Invalid Candidate ID"
            return Response({'message':message})
            print("Invalid Candidate Id")
        try:
            interviewer =Interviewer.objects.get(id=int_id)
        except Exception:
            print("invalid Interviewer ID")
            message = "Invalid Interviewer ID"
            return Response({'message':message})
        
    # Assign model values to variables for computation
        candidate_name= candidate.name
        candidate_date = candidate.date
        print(candidate_date, type(candidate_date))
        candidate_from = candidate.start_time
        print(candidate_from)
        candidate_to = candidate.end_time
        print(candidate_to)

        interviewer_name = interviewer.name
        interviewer_date = interviewer.date
        print(interviewer_date)
        interviewer_from = interviewer.start_time
        print(interviewer_from)
        interviewer_to = interviewer.end_time
        print(interviewer_to)

    #Condition to check whether the dates are same  
        if(candidate_date == interviewer_date):
            idate= candidate.date
            print ("Success")
            if candidate_from < interviewer_from and candidate_to < interviewer_from:
                print("No Avaialable Slots")
                message = "No slot available"

            elif interviewer_from < candidate_from and interviewer_to < candidate_from:
                print("No slots Available")
                message = "No slot available"

            else:
                slot_start_time = max([candidate_from, interviewer_from])
                slot_end_time = min([candidate_to, interviewer_to])

                slot_end = datetime.combine(dt.today(), slot_end_time) 
                slot_start = datetime.combine(dt.today(), slot_start_time)
                if slot_start_time and slot_end_time: 
                    if  (slot_start - slot_end).seconds < 3600:
                        print("No available slots")
                        message = "No slot available"
                    else:
                    
                        message = "Slot Available"
        else:
            message = "Date Mismatch, No slot available"
        
        return Response(
            {
                'message' : message,
                'candidate ID': can_id,
                'Candidate Name': candidate_name,
                'Interviewer ID': int_id,
                'Interviewer Name': interviewer_name,
                'date' : idate,
                'slot_start_time' : slot_start_time,
                'slot_end_time' : slot_end_time
            }
        )
 
        


        