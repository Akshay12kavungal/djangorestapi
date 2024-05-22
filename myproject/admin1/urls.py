from django.urls import path,include
from .import views
from .views import (DoctorListView, 
                    DoctorDetailView, 
                    DoctorCreateView, 
                    DoctorUpdateView,
                    DoctorDeleteView,
                    DepartmentsListView,

)

urlpatterns = [

    path('adminhome/',views.adminhome,name='adminhome'),



    #doctor
   
    path('doctors_list/', DoctorListView.as_view(), name='doctor_list'),
    path('doctors_list/create/', DoctorCreateView.as_view(), name='doctor_create'),
    path('doctors_list/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('doctors_list/update/<int:pk>/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctors_list/delete/<int:pk>/', DoctorDeleteView.as_view(), name='doctor_delete'),

    

    #department
    path('add_departments/', views.add_departments, name='add_departments'),
    path('departments_list/', views.departments_list.as_view(), name='departments_list'),
    path('booking_list/', views.booking_list, name='booking_list'),
    path('profile_list/', views.profile_list, name='profile_list'),

   
    path("depart/", DepartmentsListView.as_view(),name="department_view")


   



]