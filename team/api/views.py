from rest_framework import viewsets
from .serializers import TeamSerializer
from team.models import Team


class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class BasketbalTeamlViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint
    """
    queryset = Team.objects.filter(league__sport='baskeltball').all()
    serializer_class = TeamSerializer


class HockeyTeamViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint
    """
    queryset = Team.objects.filter(league__sport='hockey').all()
    serializer_class = TeamSerializer


class SoccerTeamViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint
    """
    queryset = Team.objects.filter(league__sport='soccer').all()
    serializer_class = TeamSerializer


class PremierLeagueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Team.objects.filter(league__name="Premier League").all()
    serializer_class = TeamSerializer
