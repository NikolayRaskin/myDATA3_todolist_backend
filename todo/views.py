from rest_framework import viewsets
from django.contrib.auth.models import User
from django.http import HttpResponse
from todo.models import Todo
from todo.serializers import UserSerializer, TodoSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


def todo(request):
    return HttpResponse("Todo")
