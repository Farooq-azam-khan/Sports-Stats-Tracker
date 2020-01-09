from rest_framework import serializers

from django.contrib.auth.models import User
from sport.models import League


class LeagueSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = League
        fields = ['name', 'sport']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
