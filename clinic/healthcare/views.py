from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.
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