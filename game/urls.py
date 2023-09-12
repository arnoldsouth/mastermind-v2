from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("game/", views.play_game, name="play_game"),
    path("history/", views.game_history, name="game_history"),
]
