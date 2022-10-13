from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from todolist.models import Task
from todolist.forms import TodoListForm
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers

import datetime

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user)
    context = {
        'list_task': data_todolist,
        'nama': 'Rafif Naufal Rahmadika',
        'npm': '2106636275',
    }
    return render(request, "todolist.html", context)

def show_cards(request):
    data_todolist = Task.objects.filter(user=request.user)
    context = {
        'list_task': data_todolist,
    }
    return render(request, "todolist_cards.html", context)

def delete_status(request):
    if request.method == "POST":
        # Task.objects.get(pk=request.DELETE['delete-id']).delete()
        Task.objects.get(pk=request.POST["task_id"]).delete()
    return redirect('todolist:show_todolist')

def delete_status_cards(request):
    if request.method == "POST":
        # Task.objects.get(pk=request.DELETE['delete-id']).delete()
        Task.objects.get(pk=request.POST["task_id"]).delete()
    return redirect('todolist:show_cards')

def change_status(request):
    if request.method == "POST":
       temp = Task.objects.get(id=request.POST["task_id"])
       temp.is_finished = not temp.is_finished
       temp.save()
    return redirect('todolist:show_todolist')

def change_status_cards(request):
    if request.method == "POST":
       temp = Task.objects.get(id=request.POST["task_id"])
       temp.is_finished = not temp.is_finished
       temp.save()
    return redirect('todolist:show_cards')

def addTask(request):
    form = TodoListForm()
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = User.objects.get(username=request.user.username)
            obj.save()
            return redirect('todolist:show_todolist')

    context = {'form':form}
    return render(request, "addtask.html", context)

def views_ajax(request):
    return render(request, "todolist_ajax.html")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

def show_json(request):
    data_todolist = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data_todolist))

def addTask_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("judul")
        deskripsi = request.POST.get("deskripsi")

        new_todolist = Task(title=title, description=deskripsi, user=request.user)
        new_todolist.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()