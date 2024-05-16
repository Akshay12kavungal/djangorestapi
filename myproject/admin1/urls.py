from django.urls import path,include
from .import views



urlpatterns = [

    path('adminhome/',views.adminhome,name='adminhome'),



    #doctor
    path('add-doctor/', views.add_doctor, name='add_doctor'),
    path('doctors_list/', views.doctors_list, name='doctors_list'),
    
   


   



]