from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Task


# Create your views here.

def HomePage(request):
    context = {}
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, "base/dashboard.html", context)


def TaskPage(request):
    context = {}
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        task = Task(user=request.user, title=request.POST.get(
            "title"), description=request.POST.get("description"))
        task.save()

    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, "base/task.html", context)


def DeleteTaskPage(request, pk):
    context = {}
    if not request.user.is_authenticated:
        return redirect('login')
    try:
        task = Task.objects.get(id=pk)
        task.delete()
        return redirect("task")
    except:
        messages.error(request, f"Invalid task id of {pk}")
        return redirect("task")


def UpdateTaskPage(request, pk):
    context = {}
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        task = Task.objects.filter(id=pk).update(title=request.POST.get(
            'title'), description=request.POST.get('description'))
        return redirect('task')
    task = Task.objects.get(id=pk)
    context = {"task": task}
    return render(request, 'base/edit_task.html', context)


def LoginPage(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        print(request.method)
        user = authenticate(request,
                            username=request.POST.get("username"), password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
            context = {"username": request.POST["username"]}
    return render(request, "base/login.html", context)


def LogoutPage(request):
    logout(request)
    return redirect('login')
