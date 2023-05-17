from django.urls import path
from boards.views import (
    boards_list,
    todos_list,
    partials_create_todo,
    partials_change_status,
    partials_sort_todos,
    partials_create_board
)

app_name = "boards"

urlpatterns = [
    path("", boards_list, name="boards_list"),
    path("<int:pk>/", todos_list, name="todos_list"),
]

htmx_patterns = [
    path(
        "_create_todo/<int:board_id>/", partials_create_todo, name="partial_create_todo"
    ),
    path(
        "_mark_as_completed/<int:board_id>/<int:todo_id>/",
        partials_change_status,
        name="partial_mark_as_completed",
    ),
    path(
        "_sort_todos/<int:board_id>/",
        partials_sort_todos,
        name="partial_sort_todos",
    ),
    path(
        "_create_board/",
        partials_create_board,
        name="partials_create_board",
    ),
]

urlpatterns += htmx_patterns
