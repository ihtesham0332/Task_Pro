from django.db import models

# Create your models here.
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # NEW: We allow this to be blank because new tasks aren't completed yet!
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
    
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title'] # We only need the user to type the title!