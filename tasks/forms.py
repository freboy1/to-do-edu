from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    task = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Add a new task'}))


    class Meta:
        model = Task
        fields = '__all__'