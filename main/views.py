from django.shortcuts import render
from datetime import datetime
from .models import Todo

def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
		'today': datetime.now(),
        'app_name': 'Super Todo List'
	}
    return render(request, 'main/index.html', context=context)
