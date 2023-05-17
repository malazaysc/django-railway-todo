from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.db.models import Max

from boards.forms.todo_create import TodoCreateForm
from .models import Board, Todo

# Create your views here.
def boards_list(request):
    boards = Board.objects.all()
    context = {
        'boards': boards
    }
    return render(request, 'boards/boards.html', context)

def todos_list(request, pk):
    todos = Todo.objects.filter(board__pk=pk)
    context = {
        'todos': todos,
        'board_id': pk
    }
    return render(request, 'boards/todos.html', context)


def partials_create_todo(request, board_id):
    title = request.POST.get('title')
    board = Board.objects.get(id=board_id)
    max_ordering = board.todos.aggregate(Max('ordering'))['ordering__max'] or 0
    new_ordering = max_ordering + 1

    Todo.objects.create(
        title=title,
        board_id=board_id,
        ordering=new_ordering
    )

    todos = Todo.objects.filter(board__pk=board_id)

    context = {
        'todos': todos,
        'board_id': board_id
    }

    return render(request, 'boards/partials/todos_list.html', context)

def partials_change_status(request, board_id, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = not todo.completed
    todo.save()

    todos = Todo.objects.filter(board__pk=board_id)

    context = {
        'todos': todos,
        'board_id': board_id
    }

    return render(request, 'boards/partials/todos_list.html', context)

def partials_sort_todos(request, board_id):
    # Get new order of todos
    todos_ordering: list[str] = request.POST.getlist('todos')
    completed_ordering: list[str] = request.POST.getlist('todos-completed')

    # get all todos
    todos = Todo.objects.filter(board__pk=board_id)

    for todo in todos:
        new_order = todos_ordering.index(str(todo.id)) if str(todo.id) in todos_ordering else completed_ordering.index(str(todo.id))
        todo.completed = str(todo.id) in completed_ordering
        todo.ordering = new_order
        
    Todo.objects.bulk_update(todos, ['ordering', 'completed'])

    todos = Todo.objects.filter(board__pk=board_id)

    context = {
        'todos': todos,
        'board_id': board_id
    }

    return render(request, 'boards/partials/todos_list.html', context)

def partials_create_board(request):
    name = request.POST.get('name')

    Board.objects.create(
        name=name
    )

    boards = Board.objects.all()

    context = {
        'boards': boards
    }

    return render(request, 'boards/partials/boards_list.html', context)