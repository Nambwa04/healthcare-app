from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DateOfBirth = models.DateField()
    PhoneNumber = models.CharField(max_length=20)
    Email = models.EmailField()
    HealthInsurance = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    PhoneNumber = models.CharField(max_length=20)
    Email = models.EmailField()
    Department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    
class Appointment(models.Model):
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    PhoneNumber = models.CharField(max_length=20)
    Email = models.EmailField()
    Date = models.DateField()
    Time = models.TimeField()
    Department = models.CharField(max_length=100)
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Reason = models.TextField()

    def __str__(self):
        return self.Patient.user.username