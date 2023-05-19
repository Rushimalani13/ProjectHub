from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.Login, name="login"),
    path('signup/', views.Signup, name="signup"),
    path('logout', views.Logout, name="logout"),
    path('profile/', views.Profile, name="profile"),
    path('editprofile/', views.EditProfile, name="editprofile"),
    path('teachersignup/',views.teacherSignup, name="teachersignup"),
]
