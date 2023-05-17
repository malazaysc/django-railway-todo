from django import forms
from boards.models import Board, Todo

class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed']
