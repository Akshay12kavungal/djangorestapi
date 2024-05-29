from django.urls import path, include
from . import views
from .views import login_view
from customer.api.views import LoginAPI

from rest_framework.routers import DefaultRouter
from customer.api.views import(
     DepartmentSerializerViewset,
     DoctorsSerializerViewset,
     BookingSerializerViewset,
     ContactSerializerViewset,
     ProfileSerializerViewset,
     UserSerializerViewset,
     


)
from rest_framework.permissions import AllowAny


router = DefaultRouter()
router.register(r'department-api', DepartmentSerializerViewset, basename='department-router')
router.register(r'doctor-api', DoctorsSerializerViewset, basename='doctor-router')
router.register(r'booking-api', BookingSerializerViewset, basename='booking-router')
router.register(r'contact-api', ContactSerializerViewset, basename='contact-router')
router.register(r'profile-api', ProfileSerializerViewset, basename='profile-router')
router.register(r'registeration-api', UserSerializerViewset, basename='registeration-router')




class CustomAPIRootView(DefaultRouter.APIRootView):
    permission_classes = [AllowAny]


router.APIRootView = CustomAPIRootView

router_urls = [
    path('api/', include(router.urls)),
    path('api/login-api/', LoginAPI.as_view(), name='login_api'),
]

urlpatterns = [

#customer   
    path('', views.home, name='home'),
    path('customerdashboard/', views.customerdashboard, name='customerdashboard'),
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='booking'),
    path('doctors/', views.doctors, name='doctors'),
    path('contact/', views.contact, name='contact'),
    path('departments/', views.departments, name='departments'),
    path('Register/', views.Register, name='Register'),
    path('logout/', views.Logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('my_appointments/', views.my_appointments, name='my_appointments'),


    path('login/', login_view, name='login'),

    path('check_username/', views.check_username, name='check_username'),
]


urlpatterns += router_urls




