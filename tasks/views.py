from django.shortcuts import render, redirect
from django.utils import timezone # NEW: Gives us the exact current time
from .models import Task
from .forms import TaskForm

# --- FUNCTION 1: The Homepage (List & Add) ---
def index(request):
    # NEW: Split tasks into two different lists!
    pending_tasks = Task.objects.filter(completed=False).order_by('-created_at')
    completed_tasks = Task.objects.filter(completed=True).order_by('-completed_at')
    
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    # Send both lists to the HTML
    context = {'pending_tasks': pending_tasks, 'completed_tasks': completed_tasks, 'form': form}
    return render(request, 'tasks/list.html', context)


# --- FUNCTION 2: The Edit Page (Update & Timestamp Logic) ---
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            # NEW: Pause before saving to check the checkbox status
            task_instance = form.save(commit=False) 
            
            # If checked as done, and doesn't have a time yet, stamp it!
            if task_instance.completed and task_instance.completed_at is None:
                task_instance.completed_at = timezone.now()
            # If user un-checks the box, remove the completed time
            elif not task_instance.completed:
                task_instance.completed_at = None
                
            task_instance.save() # Now save to database
            return redirect('/')

    context = {'form': form}
    return render(request, 'tasks/update_task.html', context)


# --- FUNCTION 3: The Delete Page ---
def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'tasks/delete_task.html', context)

# --- FUNCTION 4: Quick Complete ---
def completeTask(request, pk):
    task = Task.objects.get(id=pk)
    task.completed = True
    task.completed_at = timezone.now()
    task.save()
    return redirect('/')


# --- FUNCTION 5: Undo Complete ---
def undoTask(request, pk):
    task = Task.objects.get(id=pk)
    task.completed = False
    task.completed_at = None # Erase the timestamp!
    task.save()
    return redirect('/')


# --- FUNCTION 6: Static Pages ---
def privacyPolicy(request):
    return render(request, 'tasks/privacy.html')

def termsOfService(request):
    return render(request, 'tasks/terms.html')

def support(request):
    return render(request, 'tasks/support.html')