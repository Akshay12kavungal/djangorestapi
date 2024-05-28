from rest_framework import serializers
from customer.models import (
    Departments,
    Doctors,
    Booking,
    Profile,
    Contact,

)


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields ="__all__"

class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields ="__all__"

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields ="__all__"
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields ="__all__"
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields ="__all__"
