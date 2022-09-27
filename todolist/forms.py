from django import forms
from todolist.models import Task

class TodoListForm(forms.ModelForm):
    class Meta:
        model = Task
        # fields = '__all__'
        exclude = ('user', 'is_finished',)
