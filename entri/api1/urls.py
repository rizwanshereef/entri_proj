from django.urls import include,path
from rest_framework import routers
from .import views

router = routers.DefaultRouter()
router.register(r'candidates', views.CandidateViewSet)
router.register(r'interviewer', views.InterviewerViewSet)

urlpatterns =[
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
]