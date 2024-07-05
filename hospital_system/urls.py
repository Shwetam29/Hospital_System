
from django.contrib import admin
from django.urls import path
from app.views import home,login,patient_dashboard,doctor_dashboard,signin,signout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('patient_dashboard',patient_dashboard,name="patient_dashboard"),
    path('doctor_dashboard',doctor_dashboard,name="doctor_dashboard"),
    path('login',login,name="login"),
    path('signin',signin,name="signin"),
    path('signout',signout,name="logout"),
   
]
