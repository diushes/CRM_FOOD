from rest_framework import serializers
from .models import User, Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    dateofadd = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = ( 'id','name','surname', 'email', 'roleid',
                  'dateofadd', 'phone', 'login', 'password')
        #extra_kwargs = {'password': {'write_only': True}}