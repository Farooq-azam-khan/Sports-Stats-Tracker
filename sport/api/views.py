from rest_framework import viewsets
from sport.api.serializers import LeagueSerializer
from sport.models import League
from django.contrib.auth.models import User
from rest_framework import generics


class LeagueViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint
    """
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


class BasketballLeagueViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint
    """
    queryset = League.objects.filter(sport='basketball')
    serializer_class = LeagueSerializer


class SoccerLeagueViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint
    """
    queryset = League.objects.filter(sport="soccer")
    serializer_class = LeagueSerializer


class HockeyLeagueViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint
    """
    queryset = League.objects.filter(sport="hockey").all()
    serializer_class = LeagueSerializer
