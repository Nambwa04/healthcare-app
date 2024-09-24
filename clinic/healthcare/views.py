from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")

        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            messages.success(request, "Account created successfully.")
            return redirect('login')
        
    return render(request, 'register.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        user = authenticate(username=username, password=password, email=email)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('login')
    return render(request, 'login.html', {})

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