from django.shortcuts import render
from .models import Games
from rest_framework import generics
from .serializers import GameSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser,AllowAny


class GameCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, AllowAny)
    queryset = Games.objects.all()
    serializer_class = GameSerializer

class GameList(generics.ListAPIView):
    permission_classes = (IsAuthenticated, AllowAny)
    queryset = Games.objects.all()
    serializer_class = GameSerializer

class GameDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Games.objects.all()
    serializer_class = GameSerializer

class GameUpdate(generics.RetrieveUpdateAPIView):
    queryset = Games.objects.all()
    serializer_class = GameSerializer

class GameDelete(generics.RetrieveDestroyAPIView):
    queryset = Games.objects.all()
    serializer_class = GameSerializer
