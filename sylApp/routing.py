from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/<int:room_id>/<int:user_id>', consumers.SYLConsumer.as_asgi()),
]