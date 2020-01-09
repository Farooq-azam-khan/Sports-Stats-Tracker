from rest_framework import serializers

from team.models import Team


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    league = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Team
        fields = ['name', 'location', 'arena_name',
                  'wins', 'ties', 'losses', 'league']
