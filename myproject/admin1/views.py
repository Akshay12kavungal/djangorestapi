from django.shortcuts import render,redirect
from .forms import DoctorForm,DepartmentsForm
from customer.models import Doctors,Departments,Booking,Profile
from django.contrib.auth import authenticate,login,logout




# Create your views here.


def adminhome(request):
    return render(request,'admin/home.html')


def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('doctors_list')  
    else:
        form = DoctorForm()
    return render(request, 'admin/add_doctor.html', {'form': form})

def doctors_list(request):
    doctors = Doctors.objects.all()
    return render(request, 'admin/doctors_list.html', {'doctors': doctors})



def add_departments(request):
    if request.method=="POST":
        cont_form=DepartmentsForm(request.POST)
        if cont_form.is_valid():
            cont_form.save()
            return redirect('adminhome')
    cont_form=DepartmentsForm()
    dict_form={
        'cont_form':cont_form
    }
    return render(request,'admin/add_departments.html',dict_form)


def departments_list(request):
    dept = Departments.objects.all()
    return render(request, 'admin/departments_list.html', {'dept': dept})


def booking_list(request):
    booking=Booking.objects.all()
    return render(request,'admin/booking_list.html',{'booking':booking})

def profile_list(request):
    profile=Profile.objects.all()
    return render(request,'admin/profile_list.html',{'profile':profile})


