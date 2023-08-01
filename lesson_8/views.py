from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny

from rest_framework.views import APIView
from rest_framework import viewsets

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from lesson_6.models import GameModel, GamerModel
from lesson_7.serializers import GameModelSerializer
from lesson_8.serializers import UserSerializer

from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK


@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
def user_login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please enter username and password'})
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid data'})

    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=HTTP_200_OK)


class CreateUser(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


@csrf_exempt
@api_view(['GET', 'POST'])
def view_function(request):
    print(request.data)
    return Response({'test': 'some_data'})


class ClassAPIView(APIView):
    def get(self, request):
        return Response({'class': 'some_class_data'})

    def post(self, request):
        print(request.data)
        return Response({'class': 'some_class_data'})


class ViewSetAPIView(viewsets.ViewSet):
    queryset = GameModel.objects.filter(id__lt=10)

    def list(self, request):
        serializer = GameModelSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = GameModelSerializer(user)
        return Response(serializer.data)


class MyCreateAPIView(CreateAPIView):
    serializer_class = GameModelSerializer


class MyRetrieveAPIView(RetrieveAPIView):
    queryset = GamerModel.objects.all()
    serializer_class = GameModelSerializer


class MyRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = GamerModel.objects.all()
    serializer_class = GameModelSerializer
