from rest_framework import routers

from django.urls import path, include
from .views import todo, UserViewSet, TodoViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'todo', TodoViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
