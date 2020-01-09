from rest_framework import viewsets
from sport.api.serializers import UserSerializer, LeagueSerializer
from sport.models import League
from django.contrib.auth.models import User
from rest_framework import generics


class LeagueViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


class SoccerLeagueViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = League.objects.filter(sport="soccer")
    serializer_class = LeagueSerializer


class HockeyLeagueViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = League.objects.filter(sport="hockey").all()
    serializer_class = LeagueSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
