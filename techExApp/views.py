from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Player
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q


class PlayerListView(ListView):
    model = Player
    template_name = 'player_list.html'
    context_object_name = 'players'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Player.objects.filter(Q(name__icontains=query))
        else:
            return Player.objects.all()

class AddPlayer(CreateView):
    model = Player
    fields = ['name', 'age', 'nation', 'position', 'number']
    template_name = 'add_player.html'
    success_url = reverse_lazy('player_list')

class PlayerEditView(UpdateView):
    model = Player
    template_name = 'player_edit.html'
    fields = ['name', 'age', 'nation', 'position', 'number']
    success_url = reverse_lazy('player_list')

def delete_player(request, pk):
    player = get_object_or_404(Player, pk=pk)
    player.delete()
    return redirect('player_list')
