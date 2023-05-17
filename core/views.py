from django.shortcuts import render
from boards.models import Board

# Create your views here.
def index(request):
    boards = Board.objects.all()
    context = {
        'boards': boards
    }
    return render(request, 'core/index.html', context)
