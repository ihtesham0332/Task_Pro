from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title'] # <-- Changed this back to only the title!
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl bg-slate-50 border border-slate-200 focus:bg-white focus:ring-2 focus:ring-indigo-500 transition-all outline-none text-slate-700 placeholder-slate-400 shadow-sm',
                'placeholder': 'What do you need to do?'
            }),
        }