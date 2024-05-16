from django.shortcuts import render,redirect
from .forms import DoctorForm
from customer.models import Doctors




# Create your views here.


def adminhome(request):
    return render(request,'admin/home.html')


def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminhome')  
    else:
        form = DoctorForm()
    return render(request, 'admin/add_doctor.html', {'form': form})

def doctors_list(request):
    doctors = Doctors.objects.all()
    return render(request, 'admin/doctors_list.html', {'doctors': doctors})
