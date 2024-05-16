from django.contrib.auth.models import User
from django.db import models



# Create your models here.

class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()

    def __str__(self):
        return self.dep_name

class Doctors(models.Model):
    doc_name =models.CharField(max_length=100)
    doc_spec =models.CharField(max_length=100)
    dep_name =models.ForeignKey(Departments, on_delete=models.CASCADE)
    dep_image = models.ImageField(upload_to='doctors')

    def __str__(self):
        return 'Dr ' + self.doc_name + ' - (' + self.doc_spec + ')'


class Booking(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    p_name =models.CharField(max_length=100)
    p_phone =models.CharField(max_length=100)
    p_email =models.EmailField()
    doc_name =models.ForeignKey(Doctors, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on =models.DateField(auto_now=True)


    def __str__(self):
        return (f'{self.p_name} - {self.booking_date}') 


class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    email=models.EmailField(blank=True)
    profile_pic=models.ImageField(default='profile_pic/dq.jpg',upload_to='profile_pic')
   


    def __str__(self):
        return str(self.user)
   

