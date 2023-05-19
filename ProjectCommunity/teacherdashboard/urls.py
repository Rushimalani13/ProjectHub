from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from teacherdashboard import views

urlpatterns = [
  path('dashboard', views.Dashboard, name="dashboard"),
  path('events',views.Events, name="events"), 
]
