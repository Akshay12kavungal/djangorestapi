from django.urls import path,include
from .import views
from .views import login_view



urlpatterns = [

    path('',views.home,name='home'),
    path('customerdashboard',views.customerdashboard,name='customerdashboard'),
    
    path('about/',views.about,name='about'),
    path('booking/',views.booking,name='booking'),
    path('doctors/',views.doctors,name='doctors'),
    path('contact/',views.contact,name='contact'),
    path('departments/',views.departments,name='departments'),
    path('Register/',views.Register,name='Register'),
    #path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('my_appointments/', views.my_appointments, name='my_appointments'),

    path('login/', login_view, name='login'),  # URL for the login page
    #htmx
    path('check_username/', views.check_username, name='check_username'),
   

]

