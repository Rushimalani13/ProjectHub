from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
   path('allproject', views.allProject, name="allproject"),
   path('collegelist', views.college_List, name="collegelist"),
   path('upload', views.Upload, name="upload"),
   path('treanding', views.treandingProject, name="treanding"),
   path('aboutus', views.aboutUs, name="aboutus"),
   
]
