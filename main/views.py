from django.shortcuts import render, get_object_or_404, redirect
#from django.http import Http404
from django.contrib import messages
from datetime import datetime
from .models import Todo
from .forms import TodoForm

def index(request):
    #todos = Todo.objects.all()
    # due_date in ascending order
    todos = Todo.objects.order_by('due_date')
    # due_date in descending order
    #todos = Todo.objects.order_by('-due_date')
    # not done first
    #todos = Todo.objects.all().order_by('done')
    # done first
    #todos = Todo.objects.order_by('-done')

    context = {
        'todos': todos,
        'today': datetime.now(),
        'app_name': 'Super Todo List'
    }
    return render(request, 'main/index.html', context=context)

def todo_detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)

    context = {
        'todo': todo
    }
    return render(request, 'main/todo_detail.html', context=context)

def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "The todo was created successfully")
            return redirect('index')
        return render(request, 'main/todo.html', {'form': form})
    return render(request, 'main/todo.html', {'form': TodoForm()})

def todo_update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, "The todo was updated successfully")
            return redirect('index')
        return render(request, 'main/todo.html', {'form': form})
    return render(request, 'main/todo.html', {'form': TodoForm(instance=todo)})

def todo_delete(request, todo_id):
	"""Delete an existing todo."""
	todo = get_object_or_404(Todo, pk=todo_id)
	todo.delete()
	return redirect('index')
