from django.contrib import admin
from .models import Candidate, Interviewer


admin.site.register(Candidate) #Register Model Candidate
admin.site.register(Interviewer) #Register Model Interviewer
