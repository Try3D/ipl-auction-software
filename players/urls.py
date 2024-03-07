from django.urls import path
from . import views

urlpatterns = [
    path("getPlayer/<str:pk>/", views.player, name="get_player"),
    path("", views.index),
    path("addplayer", views.addplayer),
    path("player_rtm", views.player_rtm),
]
