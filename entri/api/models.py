from django.db import models

#model for candidate
class Candidate(models.Model): 
    candidate_id= models.IntegerField(primary_key=True, blank= False)
    name= models.CharField(max_length=100)
    email_address = models.EmailField()
    phone= models.IntegerField()
    date= models.DateField()
    start_time =  models.TimeField()
    end_time = models.TimeField()

  

#model for Interviewer
class Interviewer(models.Model):
    interviewer_id = models.IntegerField(primary_key= True ,blank=False)
    name= models.CharField(max_length=100)
    date= models.DateField()
    start_time =  models.TimeField()
    end_time = models.TimeField()

    