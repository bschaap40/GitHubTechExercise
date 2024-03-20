from django.urls import path
from . import views
from .views import AddPlayer, PlayerListView

urlpatterns = [
    path('', PlayerListView.as_view(), name='player_list'),
    path('add/', AddPlayer.as_view(), name='add_player')
]
