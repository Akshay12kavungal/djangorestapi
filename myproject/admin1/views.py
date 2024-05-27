from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from .forms import DoctorForm,DepartmentsForm
from customer.models import Doctors,Departments,Booking,Profile
from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse

from django_tables2 import SingleTableView
from .tables import DepartmentTable,DoctorsTable




# Create your views here.


def adminhome(request):
    return render(request,'admintemplate/home.html')

# table2

class Doctor2ListView(SingleTableView):
    model = Doctors
    template_name = 'admintemplate/doctor/list.html'
    context_object_name = 'doctors2'
    table_class = DoctorsTable

class Doctor2DetailView(DetailView):
    model = Doctors
    template_name = 'admintemplate/doctor/detail.html'
    context_object_name = 'doctor2'

class Doctor2CreateView(CreateView):
    model = Doctors
    form_class = DoctorForm
    template_name = 'admintemplate/doctor/create.html'

    def get_success_url(self):
        return reverse('doctor2_list')

class Doctor2UpdateView(UpdateView):
    model = Doctors
    form_class = DoctorForm
    template_name = 'admintemplate/doctor/update.html'

    def get_success_url(self):
        return reverse('doctor2_list')

class Doctor2DeleteView(DeleteView):
    model = Doctors
    template_name = 'admintemplate/doctor/delete.html'
    context_object_name = 'doctor2'

    def get_success_url(self):
        return reverse('doctor2_list')


# def add_doctor(request):
#     if request.method == 'POST':
#         form = DoctorForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('doctors_list')  
#     else:
#         form = DoctorForm()
#     return render(request, 'admin/add_doctor.html', {'form': form})

# def doctors_list(request):
#     doctors = Doctors.objects.all()
#     return render(request, 'admin/doctors_list.html', {'doctors': doctors})



class DoctorListView(ListView):
    model = Doctors
    template_name = 'admintemplate/doctor_list.html'
    context_object_name = 'doctors'

class DoctorDetailView(DetailView):
    model = Doctors
    template_name = 'admintemplate/doctor_detail.html'
    context_object_name = 'doctor'

class DoctorCreateView(CreateView):
    model = Doctors
    template_name = 'admintemplate/doctor_form.html'
    fields = ['doc_name', 'doc_spec', 'dep_name','dep_image']

    def get_success_url(self):
        return reverse('doctor_list')

class DoctorUpdateView(UpdateView):
    model = Doctors
    template_name = 'admintemplate/doctor_form.html'
    fields = ['doc_name', 'doc_spec', 'dep_name','dep_image']

    def get_success_url(self):
        return reverse('doctor_list')
    
class DoctorDeleteView(DeleteView):
    model = Doctors
    template_name = 'admintemplate/doctor_confirm_delete.html'
    

    def get_success_url(self):
        return reverse('doctor_list')


def add_departments(request):
    if request.method=="POST":
        cont_form=DepartmentsForm(request.POST)
        if cont_form.is_valid():
            cont_form.save()
            return redirect('departments_list')
    cont_form=DepartmentsForm()
    dict_form={
        'cont_form':cont_form
    }
    return render(request,'admintemplate/add_departments.html',dict_form)

class departments_list(ListView):
    template_name ='admintemplate/departments_list.html'
    model=Departments
    context_object_name='dept'
 



def booking_list(request):
    booking=Booking.objects.all()
    return render(request,'admintemplate/booking_list.html',{'booking':booking})

def profile_list(request):
    profile=Profile.objects.all()
    return render(request,'admintemplate/profile_list.html',{'profile':profile})




class DepartmentsListView(SingleTableView):
    model = Departments
    template_name = 'admintemplate/department/list.html'
    context_object_name = 'dept'
    table_class = DepartmentTable

class DepartmentsDetailView(DetailView):
    model = Departments
    template_name = 'admintemplate/department/detail.html'
    context_object_name = 'dept'

class DepartmentsCreateView(CreateView):
    model = Departments
    form_class = DepartmentsForm
    template_name = 'admintemplate/department/create.html'

    def get_success_url(self):
        return reverse('department_list')

class DepartmentsUpdateView(UpdateView):
    model = Departments
    form_class = DepartmentsForm
    template_name = 'admintemplate/department/update.html'

    def get_success_url(self):
        return reverse('department_list')

class DepartmentsDeleteView(DeleteView):
    model = Departments
    template_name = 'admintemplate/department/delete.html'
    context_object_name = 'dept'

    def get_success_url(self):
        return reverse('department_list')
    
