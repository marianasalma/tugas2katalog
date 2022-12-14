from django.shortcuts import render
from todolist.models import Task
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core import serializers
from django.urls import reverse

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user) # mengambil object tasks miliki user yang sedang login
    context = {
        'list_todolist': data_todolist,
        'username': request.user.username,
    }
    return render(request, "todolist.html", context)

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
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create(request):
    if request.method == 'POST':
        date = datetime.date.today() 
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = request.user
        Task.objects.create(title=title, description=description, date=date, user=user)
        response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
        return response
    return render(request, "createtask.html")

def show_json(request):
    task = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', task), content_type='application/json')

def add(request):
    if request.method == 'POST':
        date = datetime.date.today() 
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = request.user
        task = Task.objects.create(title=title, description=description, date=date, user=user)

        context = {
            'pk': task.pk,
            'fields':{
                'title':task.title,
                'description':task.description,
                'is_finished':task.is_finished,
                'date':task.date,
            }
        }
        return JsonResponse(context)
        
def change_status(request,pk):
    task = Task.objects.get(id=pk)
    task.is_finished = not task.is_finished
    task.save()
    return redirect('todolist:show_todolist')