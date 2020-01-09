from django.urls import path, include
from sport.api.views import UserViewSet, LeagueViewSet, SoccerLeagueViewSet, HockeyLeagueViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'all', LeagueViewSet, basename='all-leagues')
router.register(r'soccer', SoccerLeagueViewSet, basename='soccer-leagues')
router.register(r'hockey', HockeyLeagueViewSet, basename='hockey-leagues')

urlpatterns = [
    path('', include(router.urls))
]
