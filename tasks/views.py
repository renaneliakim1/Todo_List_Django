from django.shortcuts import render, redirect , get_object_or_404

from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.order_by('-created_at')

    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:list)')
        else:
            form=TaskForm()
        return render(request, 'tasks/task_form.html', {'form' : form, 'title': 'Nova Tarefa'})

def task_toggle(request, pk): 
    task = get_object_or_404(Task, pk=pk)
    task.done = not task.done
    task.save()
    return redirect('tasks:list')


def task_edit(request, pk): 
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:list')
        else:
            form=TaskForm(instance=task)
        return render(request, 'tasks/task_form.html', {'form' : form, 'title': 'Editar Tarefa'})    
    

def task_delete(request, pk): 
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})