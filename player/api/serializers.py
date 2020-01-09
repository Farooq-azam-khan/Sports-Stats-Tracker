from rest_framework import serializers
from player.models import Player
from team.models import Team


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    team = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Player
        fields = ['first_name',
                  'last_name',
                  'number',
                  'team']
