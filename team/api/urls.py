from django.urls import path, include
from .views import (TeamViewSet,
                    SoccerTeamViewSet,
                    HockeyTeamViewSet,
                    BasketbalTeamlViewSet,
                    PremierLeagueViewSet)

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'all', TeamViewSet, basename='all-teams')
router.register(r'soccer', SoccerTeamViewSet, basename='soccer-teams')
router.register(r'hockey', HockeyTeamViewSet, basename='hockey-teams')
router.register(r'basketball', BasketbalTeamlViewSet,
                basename='basketball-teams')
router.register(r'premier-league', PremierLeagueViewSet,
                basename='premier-league-teams')


urlpatterns = [
    path('', include(router.urls))
]
