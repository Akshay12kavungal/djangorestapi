from django import forms
from customer.models import Doctors

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields ='__all__'
