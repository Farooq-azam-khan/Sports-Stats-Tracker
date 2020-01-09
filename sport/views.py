from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from sport.api.serializers import LeagueSerializer


class LeagueViewSet(viewsets.ModelViewSet):
    """
    API endpoint
    """
    queryset = User.objects.all()
    serializer_class = LeagueSerializer
