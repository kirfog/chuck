from django.urls import path

from .consumers import joke_consumer

ws_urlpatterns = [path("ws/jokes/", joke_consumer.as_asgi())]
