from django.shortcuts import render, redirect , get_object_or_404

from .models import Tasks
from .forms import TaskForm

from django.contrib.auth import login 
from django.contrib.auth.decorators import login_required
from .forms import CadastroUsuarioForm

def cadastro_usuario(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tasks:list')
    else:
        form = CadastroUsuarioForm()
        return render(request, 'cadastro_usuario.html', {'form': form})
    

@login_required
def task_list(request):
    tasks = Tasks.objects.order_by('-created_at')

    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:list')
        return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Nova Tarefa'})
    else:
        form = TaskForm()
        return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Nova Tarefa'})

def task_toggle(request, pk): 
    task = get_object_or_404(Tasks, pk=pk)
    task.done = not task.done
    task.save()
    return redirect('tasks:list')


def task_edit(request, pk): 
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:list')
        return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Editar Tarefa'})
    else:
        form = TaskForm(instance=task)
        return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Editar Tarefa'})
    

def task_delete(request, pk): 
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})