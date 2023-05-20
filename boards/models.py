from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    board = models.ForeignKey('Board', on_delete=models.CASCADE, related_name='todos')
    ordering = models.PositiveSmallIntegerField(null=True, blank=True) 
    # Order of the todo in the board, if null, it will be appended to the end of the list based on pk
    

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['ordering', 'pk']
    

class Board(models.Model):
    name = models.CharField(max_length=120)
    subject = models.CharField(max_length=255)
    """Subject will be used to generate for the GPT prompt, so it helps suggesting TODOs"""

    @property
    def not_completed_todos_count(self) -> int:
        return self.todos.filter(completed=False).count()

    def __str__(self):
        return self.name