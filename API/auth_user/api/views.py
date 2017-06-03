from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from .permissions import IsStaffOrTargetUser
from .serializers import UserAuthSerializer

class UserAuthView(CreateAPIView):
        queryset = User.objects.all()
        serializer_class = UserAuthSerializer
        # model = User

        # def get_permissions(self):
        #     return (AllowAny() if self.request.method == POST
        #         else IsStaffOrTargetUser())
