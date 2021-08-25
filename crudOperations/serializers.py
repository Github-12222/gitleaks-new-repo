from rest_framework import serializers
from .models import Games


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Games
        fields = ['id','Game_Name', 'Game_Type','Game_Content','Game_Image']
