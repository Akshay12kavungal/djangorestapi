from rest_framework import permissions,viewsets
from customer.api.serializers import (
    DepartmentSerializer,
    DoctorsSerializer,
    BookingSerializer,
    ProfileSerializer,
    ContactSerializer,

)


class DepartmentSerializerViewset(viewsets.ModelViewSet):
    serializer_class=DepartmentSerializer
    queryset=DepartmentSerializer.Meta.model.objects.all()
    permission_classes=[permissions.IsAuthenticated]

class DoctorsSerializerViewset(viewsets.ModelViewSet):
    serializer_class=DoctorsSerializer
    queryset=DoctorsSerializer.Meta.model.objects.all()
    permission_classes=[permissions.IsAuthenticated]

class BookingSerializerViewset(viewsets.ModelViewSet):
    serializer_class=BookingSerializer
    queryset=BookingSerializer.Meta.model.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    
class ProfileSerializerViewset(viewsets.ModelViewSet):
    serializer_class=ProfileSerializer
    queryset=ProfileSerializer.Meta.model.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    
class ContactSerializerViewset(viewsets.ModelViewSet):
    serializer_class=ContactSerializer
    queryset=ContactSerializer.Meta.model.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    