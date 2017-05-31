from rest_framework.serializers import ModelSerializer
from users.models import User

class UserCreateSerialier(ModelSerializer):
    class Meta:
        model = User
        exclude = ('register_date',)


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
