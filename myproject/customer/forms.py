from django import forms
from .models import Booking,Contact,Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class DateInput(forms.DateInput):
    input_type='date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'booking_date': DateInput(),
        }
        labels = {
            'p_name': "Patient Name",
            'p_phone': "Patient Phone",
            'p_email': "Patient Email",
            'doc_name': "Doctor Name",
            'booking_date': "Booking Date",
        }


class RegistrationForm(UserCreationForm):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    phone_number=forms.CharField(max_length=10)
    email=forms.EmailField()
    

    

    class Meta:
        model=User
        fields=('username','password1','password2','email','first_name','last_name','phone_number')

        


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields ='__all__'


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model =Profile
        fields=['first_name','last_name','phone_number','profile_pic']
        