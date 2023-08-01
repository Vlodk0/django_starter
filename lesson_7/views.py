from lesson_6.models import GameModel, GamerModel
from rest_framework import viewsets
from lesson_7.serializers import GameModelSerializer, GamerModelSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = GameModel.objects.all().order_by('-genre')
    serializer_class = GameModelSerializer


class GamerViewSet(viewsets.ModelViewSet):
    queryset = GamerModel.objects.all()
    serializer_class = GamerModelSerializer
