from django.urls import re_path
from . import consumers

# URLs that handle the WebSocket connection are placed here.
websocket_urlpatterns = [
    re_path(r"ws/appchat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
]
