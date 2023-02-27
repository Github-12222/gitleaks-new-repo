from rest_framework import serializers
from .models import Games


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Games
        fields = ['id','Game_Name', 'Game_Type','Game_Content','Game_Image']
AWS_SECRET_KEY = '5sVuvbO367NZYBXL7lDEs1HX3Qkz33ks0qpaiad/'
