from rest_framework import serializers
from customer.models import (
    Departments,
    Doctors,
    Booking,
    Profile,
    Contact,
    User,

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

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields =["username","first_name","last_name","email","password","confirm_password"]

    def save(self):
        reg=User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
        

        )
        password=self.validated_data['password']
        confirm_password=self.validated_data['confirm_password']

        if password!=confirm_password:
            raise serializers.ValidationError({'password':'password does not match'})
        reg.set_password(password)
        reg.save()
        Profile.objects.create(
                user=reg,
                first_name=self.validated_data['first_name'],
                last_name=self.validated_data['last_name'],
                email=self.validated_data['email'],
            )
        return reg