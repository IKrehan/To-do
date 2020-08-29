from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def home(request):

    return render(request, 'index.html', context={"tasks": Task.objects.all()})


def createTask(request):
    if request.method == "POST":
        name = request.POST.get('task-name')
        Task.objects.create(name=name)

    return redirect('home')


def deleteTask(request, pk):
    Task.objects.get(id=pk).delete()
    return redirect('home')


def updateTask(request, pk):
    if request.method == "POST":
        name = request.POST.get('task-name')
        task = Task.objects.get(id=pk)
        task.name = name
        task.save()

        return redirect('home')

    return render(request, 'update.html', context={"tasks": Task.objects.all(), 'task_edit': Task.objects.get(id=pk)})


def updateTaskStatus(request, pk):
    task = Task.objects.get(id=pk)

    if task.is_active == True:
        task.is_active = False
    
    else:
        task.is_active = True
    
    task.save()

    return redirect('home')
