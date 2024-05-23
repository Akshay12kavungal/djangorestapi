from django.urls import path,include
from .import views
from .views import (DoctorListView, 
                    DoctorDetailView, 
                    DoctorCreateView, 
                    DoctorUpdateView,
                    DoctorDeleteView,
                    DepartmentsListView,

)
from .views import Doctor2ListView, Doctor2DetailView, Doctor2CreateView, Doctor2UpdateView, Doctor2DeleteView

from .views import DepartmentsListView,DepartmentsDetailView,DepartmentsCreateView,DepartmentsUpdateView,DepartmentsDeleteView

urlpatterns = [

    path('adminhome/',views.adminhome,name='adminhome'),



    #doctor
   
    path('doctors_list/', DoctorListView.as_view(), name='doctor_list'),
    path('doctors_list/create/', DoctorCreateView.as_view(), name='doctor_create'),
    path('doctors_list/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('doctors_list/update/<int:pk>/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctors_list/delete/<int:pk>/', DoctorDeleteView.as_view(), name='doctor_delete'),



    path('doctors2/', Doctor2ListView.as_view(), name='doctor2_list'),
    path('doctors2/<int:pk>/', Doctor2DetailView.as_view(), name='doctor2_detail'),
    path('doctors2/create/', Doctor2CreateView.as_view(), name='doctor2_create'),
    path('doctors2/update/<int:pk>/', Doctor2UpdateView.as_view(), name='doctor2_update'),
    path('doctors2/delete/<int:pk>/', Doctor2DeleteView.as_view(), name='doctor2_delete'),

    

    #department
    path('add_departments/', views.add_departments, name='add_departments'),
    path('departments_list/', views.departments_list.as_view(), name='departments_list'),



    path('DepartmentsList/', DepartmentsListView.as_view(), name='department_list'),
    path('DepartmentsList/<int:pk>/', DepartmentsDetailView.as_view(), name='department_detail'),
    path('DepartmentsList/create/', DepartmentsCreateView.as_view(), name='department_create'),
    path('DepartmentsList/update/<int:pk>/', DepartmentsUpdateView.as_view(), name='department_update'),
    path('DepartmentsList/delete/<int:pk>/', DepartmentsDeleteView.as_view(), name='department_delete'),


    path('booking_list/', views.booking_list, name='booking_list'),
    path('profile_list/', views.profile_list, name='profile_list'),


    

   
    


   



]