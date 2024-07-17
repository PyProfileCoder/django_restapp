from rest_framework import serializers
from restapp.models import MyModel


class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model: MyModel
        fields: '__all__'



from django.contrib.auth.models import Group, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
    