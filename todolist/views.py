import datetime
from urllib import request
from todolist.models import Task
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from todolist.forms import CreateTask
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    todolist = Task.objects.filter(user=request.user)
    context = {
        'username' : request.user.username,
        'todolist' : todolist,
        'name' : 'Nadhif Rahman Alfan',
        'student_id' : '2106751783',
    }
    return render(request,"todolist.html", context)

@login_required(login_url='/todolist/login/')
def create_todolist(request):
    form = CreateTask()
    if request.method == "POST":
        form = CreateTask(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('todolist:show_todolist')
    context = {
        'form':form
    }
    return render(request,'create-task.html',context)

@login_required(login_url='/todolist/login/')
def delete_todolist(request,id):
    task = Task.objects.filter(id=id)[0]
    task.delete()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def update_todolist(request,id):
    task = Task.objects.filter(id=id)[0]
    task.finished = not task.finished
    task.save()
    return redirect('todolist:show_todolist')

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
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.now()))
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return redirect('todolist:login')

