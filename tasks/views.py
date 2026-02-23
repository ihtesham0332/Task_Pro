from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Task
from .forms import TaskForm
from django.contrib.auth import logout
# A quick helper function to grab the pending count for the header
def get_global_context():
    return {
        'pending_count': Task.objects.filter(completed=False).count()
    }

def index(request):
    pending_tasks = Task.objects.filter(completed=False).order_by('-created_at')
    completed_tasks = Task.objects.filter(completed=True).order_by('-completed_at')
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'pending_tasks': pending_tasks, 'completed_tasks': completed_tasks, 'form': form}
    context.update(get_global_context()) # Add the bell count!
    return render(request, 'tasks/list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    context.update(get_global_context())
    return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    context.update(get_global_context())
    return render(request, 'tasks/delete_task.html', context)

def completeTask(request, pk):
    task = Task.objects.get(id=pk)
    task.completed = True
    task.completed_at = timezone.now()
    task.save()
    return redirect('/')

def undoTask(request, pk):
    task = Task.objects.get(id=pk)
    task.completed = False
    task.completed_at = None
    task.save()
    return redirect('/')

# --- Static Pages ---
def privacyPolicy(request):
    context = get_global_context()
    return render(request, 'tasks/privacy.html', context)

def termsOfService(request):
    context = get_global_context()
    return render(request, 'tasks/terms.html', context)

def support(request):
    context = get_global_context()
    return render(request, 'tasks/support.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/') # Or redirect to a login page if you have one