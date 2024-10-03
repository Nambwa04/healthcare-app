from django.urls import path
from . import views

urlpatterns = [
   path('', views.login_user, name='login'),
   path('register/doctor/', views.register_doctor, name='register_doctor'),
   path('register/patient/', views.register_patient, name='register_patient'),
   path('home/', views.home, name='home'),
   path('contact/', views.contact, name='contact'),
   path('about/', views.about, name='about'),
   path('departments/', views.departments, name='departments'),
   path('doctors/', views.doctors, name = 'doctors'),
   path('appointment/', views.appointment, name='appointment'),
   path('video-conference/', views.video_conference, name='video_conference'),
   path('meeting/', views.meeting, name='meeting'),
   path('join-room/', views.join_room, name='join_room'),
]
