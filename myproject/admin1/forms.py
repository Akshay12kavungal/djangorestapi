from django import forms
from customer.models import Doctors,Departments

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields ='__all__'

        
class DepartmentsForm(forms.ModelForm):
    class Meta:
        model = Departments
        fields ='__all__'




