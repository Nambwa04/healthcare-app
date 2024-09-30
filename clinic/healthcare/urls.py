from django.urls import path
from . import views

urlpatterns = [
   path('', views.login_user, name='login'),
   path('register.html', views.register, name='register'),
   path('home.html', views.home, name='home'),
   path('contact.html', views.contact, name='contact'),
   path('about.html', views.about, name='about'),
   path('departments.html', views.departments, name='departments'),
   path('doctors.html', views.doctors, name = 'doctors'),
   path('appointment.html', views.appointment, name='appointment'),
   path('video_conference.html', views.video_conference, name='video_conference'),
   path('meeting.html', views.meeting, name='meeting'),
   path('join_room', views.join_room, name='join_room'),
]
