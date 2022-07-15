from django.urls import path, include
from sylApp.views import CreateRoomViewset
from rest_framework import routers

urlpatterns = [
    path('', CreateRoomViewset.as_view(), name='create_room'),
]