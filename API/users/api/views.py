# from django.shortcuts import render
from rest_framework.generics import (
                                    ListAPIView,
                                    RetrieveAPIView,
                                    DestroyAPIView,
                                    UpdateAPIView,
                                    CreateAPIView,
                                    )

from users.models import User
from .serializers import (
                            UserSerializer,
                            UserDetailSerializer,
                            UserCreateSerialier,
                            )

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

class UserDelete(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

class UserUpdate(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerialier
