from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Player
from django.http import HttpResponse

class PlayerListView(ListView):
    model = Player
    template_name = 'player_list.html'
    context_object_name = 'players'

class AddPlayer(CreateView):
    model = Player
    fields = ['name', 'age', 'position', 'number']
    template_name = 'add_player.html'
    success_url = reverse_lazy('player_list')

