from django.urls import include, path
from customer.api.views import(
     DepartmentSerializerViewset,
     DoctorsSerializerViewset,
     BookingSerializerViewset,
     ContactSerializerViewset,
     ProfileSerializerViewset,
     UserSerializerViewset,
     


)

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'department', DepartmentSerializerViewset)
router.register(r'doctor', DoctorsSerializerViewset)
router.register(r'booking', BookingSerializerViewset)
router.register(r'contact', ContactSerializerViewset)
router.register(r'profile', ProfileSerializerViewset)
router.register(r'registeration', UserSerializerViewset)

urlpatterns = [
    path('', include(router.urls))
]

