from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('register.html', views.register, name='register'),
   path('login.html', views.login_user, name='login'),
   path('contact.html', views.contact, name='contact'),
   path('about.html', views.about, name='about'),
   path('departments.html', views.departments, name='departments'),
   path('doctors.html', views.doctors, name = 'doctors'),
   
]
