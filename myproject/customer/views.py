from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

from .models import Departments,Doctors,Booking,Profile,Contact
from .forms import BookingForm,RegistrationForm,ContactForm,ProfileUpdateForm

from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from django.contrib.auth import get_user_model



def customerdashboard(request):
    return render(request,'customer/customerdashboard.html')

def home(request):
    return render(request,'customer/home.html')

def Register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()  
            Profile.objects.create(
                user=user,
                first_name=user_form.cleaned_data['first_name'],
                last_name=user_form.cleaned_data['last_name'],
                phone_number=user_form.cleaned_data['phone_number'],
                email=user_form.cleaned_data['email'],
            )
         
            return redirect('login')
    else:
        user_form = RegistrationForm()
    return render(request, 'registration/registration.html', {'user_form': user_form})

def check_username(request):
    username=request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<div style='color:red;'>The username already exists")

    else:
        return HttpResponse("<div style='color:green;'>The username is available")



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if role == 'admin' and user.is_superuser:
                login(request, user)
                messages.success(request, 'You have successfully logged in as admin.')
                return redirect('adminhome')
            else:
                login(request, user)
                messages.success(request, 'You have successfully logged in as customer.')
                return redirect('customerdashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'registration/login.html')

# def login_view(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']

#         user= authenticate(username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return render(request,'customer/customerdashboard.html')

#         else:
#             return render(request,'registration/login.html')

#     else:
#         return render(request,'registration/login.html')

def Logout(request):
    logout(request)
    return redirect('home')

def about(request):
    return render(request,'customer/about.html')

def booking(request):
    if request.method =="POST":
        form =BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'customer/conformation.html')
    form= BookingForm()
    dict_form ={
        'form': form
    }
    return render(request,'customer/booking.html',dict_form)

def doctors(request):

    dict_docs ={
        'doctors': Doctors.objects.all()
    }

    return render(request,'customer/doctors.html',dict_docs)

def contact(request):
    if request.method=="POST":
        cont_form=ContactForm(request.POST)
        if cont_form.is_valid():
            cont_form.save()
            return redirect('customerdashboard')
    cont_form=ContactForm()
    dict_form={
        'cont_form':cont_form
    }
    return render(request,'customer/contact.html',dict_form)

def departments(request):

    dict_dept={
        'dept':Departments.objects.all()
    }
    
    return render(request,'customer/departments.html',dict_dept)





def profile(request):
    user = request.user
    profile = user.profile 
    return render(request, 'customer/profile.html', {'user': user, 'profile': profile})


def profile_update(request):
    user = request.user
    profile = user.profile
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'customer/profile_update.html', {'form': form})


def my_appointments(request):
    user_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'customer/my_appointments.html', {'user_bookings': user_bookings})


