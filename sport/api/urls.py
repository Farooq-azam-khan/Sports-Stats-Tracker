from django.urls import path, include
from sport.api.views import (LeagueViewSet,
                             SoccerLeagueViewSet,
                             HockeyLeagueViewSet,
                             BasketballLeagueViewSet)

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'all', LeagueViewSet, basename='all-leagues')
router.register(r'soccer', SoccerLeagueViewSet, basename='soccer-leagues')
router.register(r'hockey', HockeyLeagueViewSet, basename='hockey-leagues')
router.register(r'basketball', BasketballLeagueViewSet,
                basename='basketball-leagues')

urlpatterns = [
    path('', include(router.urls))
]
