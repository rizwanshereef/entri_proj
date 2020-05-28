from django.urls import include,path
from rest_framework import routers
# from .import views
from .views import HRView,CandidateViewSet, InterviewerViewSet

# inp=views.HRViewSet
router = routers.DefaultRouter()
router.register(r'candidates', CandidateViewSet)
router.register(r'interviewer', InterviewerViewSet)
urlpatterns =[
    path('',include(router.urls)),
    path('hr/',HRView.as_view(), name="Input"),

]