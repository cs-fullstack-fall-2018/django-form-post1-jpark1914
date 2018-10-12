from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import VideoGame
from .forms import VideoGameForm
from django.utils import timezone
from django.shortcuts import redirect
# Create your views here.
def home(request):
    return render(request, 'vicar_app/base.html')

def index(request):
    game_list = VideoGame.objects.all()
    context = {'game_list':game_list}
    return render(request, 'vicar_app/index.html', context)

def detail(requests, pk):
    game = get_object_or_404(VideoGame,pk=pk)
    context = {'game':game}
    return render(requests, 'vicar_app/detail.html',context)

def add(request):
    if request.method == 'POST':
        form = VideoGameForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        return redirect('game', pk=post.pk)
    else:
        form = VideoGameForm()

    return render(request, 'vicar_app/add.html', {'form':form})