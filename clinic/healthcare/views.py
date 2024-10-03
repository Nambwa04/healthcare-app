from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import AppointmentForm, UserForm, DoctorForm, PatientForm

# Create your views here.

def register_doctor(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        doctor_form = DoctorForm(request.POST)
        if user_form.is_valid() and doctor_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            doctor = doctor_form.save(commit=False)
            doctor.user = user
            doctor.save()
            login(request, user)
            messages.success(request, 'Doctor registration successful.')
            return redirect('home')
        
    else:
        user_form = UserForm()
        doctor_form = DoctorForm()
        return render(request, 'register_doctor.html', {'user_form': user_form, 'doctor_form': doctor_form})
    
def register_patient(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        patient_form = PatientForm(request.POST)
        if user_form.is_valid() and patient_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            patient = patient_form.save(commit=False)
            patient.user = user
            patient.save()
            login(request, user)
            messages.success(request, 'Patient registration successful.')
            return redirect(reverse('login'))
    else:
            user_form = UserForm()
            patient_form = PatientForm()
    return render(request, 'register_patient.html', {'user_form': user_form, 'patient_form': patient_form})

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        if not User.objects.filter(username=username).exists():
            messages.error(request, "User does not exist. Please register.")
            return redirect('register')

        user = authenticate(username=username, password=password, email=email)

        if user is not None:
            login(request, user)
            if request.user.is_authenticated:
                messages.success(request, "Login successful.")
                return redirect('home')
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('login')
    return render(request, 'login.html', {})

@login_required
def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == 'POST':
        FullName = request.POST.get('FullName', '')
        Phone = request.POST.get('Phone', '')
        Email = request.POST.get('Email', '')
        Message = request.POST.get('Message', '')

        return HttpResponse('Thank you for your message! We will get back to you soon!')
    return render(request, 'contact.html', {})

        # return render(request, 'contact.html', {'FullName': FullName, 'Phone': Phone, 'Email': Email, 'Message': Message})
    
        # # Send an email
        # send_mail(
        #     FullName, #username
        #     Phone, #phone
        #     Email, #email
        #     [settings.EMAIL_HOST_USER], #email
        #     Message, #message
        # )

    # else:
    #     return render(request, 'contact.html', {})
    
def about(request):
    return render(request, 'about.html', {})

def departments(request):
    return render(request, 'departments.html', {})

def doctors(request):
    return render(request, 'doctors.html', {})

def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Thank you for booking an appointment with us!')

    else:
        form = AppointmentForm()
        return render(request, 'appointment.html', {'form': form})

def video_conference(request):
    return render(request, 'video_conference.html', {})

def meeting(request):
    return render(request, 'meeting.html', {})

def join_room(request):
    return render(request, 'join_room.html', {})