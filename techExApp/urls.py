from django.urls import path
from .views import AddPlayer, PlayerListView, PlayerEditView, delete_player

urlpatterns = [
    path('', PlayerListView.as_view(), name='player_list'),
    path('add/', AddPlayer.as_view(), name='add_player'),
    path('players/<int:pk>/edit/', PlayerEditView.as_view(), name='player_edit'),
    path('delete/<int:pk>/', delete_player, name='delete_player'),
]
