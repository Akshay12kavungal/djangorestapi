from rest_framework import permissions,viewsets
from customer.api.serializers import (
    DepartmentSerializer,
    DoctorsSerializer,
    BookingSerializer,
    ProfileSerializer,
    ContactSerializer,
    UserSerializer,

)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

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

class UserSerializerViewset(viewsets.ModelViewSet):
    serializer_class=UserSerializer
    queryset=UserSerializer.Meta.model.objects.all()
    permission_classes=[permissions.IsAuthenticated]



class LoginAPI(APIView):
    def post(self,request,*args,**kwargs):
        username=request.data.get('username')
        password=request.data.get('password')

        user=authenticate(username=username,password=password)

        if user:
            token,_=Token.objects.get_or_create(user=user)
            return Response({'token':token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error':'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    

