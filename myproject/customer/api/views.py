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
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

from rest_framework import generics,mixins
from django.contrib.auth.models import User

class DepartmentSerializerViewset(viewsets.ModelViewSet):
    serializer_class=DepartmentSerializer
    queryset=DepartmentSerializer.Meta.model.objects.all()
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]

class DoctorsSerializerViewset(viewsets.ModelViewSet):
    serializer_class=DoctorsSerializer
    queryset=DoctorsSerializer.Meta.model.objects.all()
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]

class BookingSerializerViewset(viewsets.ModelViewSet):
    serializer_class=BookingSerializer
    queryset=BookingSerializer.Meta.model.objects.all()
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
class ProfileSerializerViewset(viewsets.ModelViewSet):
    serializer_class=ProfileSerializer
    queryset=ProfileSerializer.Meta.model.objects.all()
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
class ContactSerializerViewset(viewsets.ModelViewSet):
    serializer_class=ContactSerializer
    queryset=ContactSerializer.Meta.model.objects.all()
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]

class UserSerializerViewset(viewsets.ModelViewSet):
    serializer_class=UserSerializer
    queryset=UserSerializer.Meta.model.objects.all()
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]



class LoginAPI(APIView):
    permission_classes = [AllowAny]
    def post(self,request,*args,**kwargs):
        username=request.data.get('username')
        password=request.data.get('password')

        user=authenticate(username=username,password=password)

        if user:
            token,_=Token.objects.get_or_create(user=user)
            return Response({'token':token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error':'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    


class UserList(generics.ListCreateAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self,request,*args,**kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserRetrieveUpdateDestroyAPIView(generics.GenericAPIView, 
                                       mixins.RetrieveModelMixin, 
                                       mixins.UpdateModelMixin, 
                                       mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    