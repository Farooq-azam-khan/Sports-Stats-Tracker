from rest_framework import viewsets
from .serializers import PlayerSerializer
from player.models import Player


class PlayerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
