from django.urls import path
from todolist.views import show_todolist
from todolist.views import register 
from todolist.views import login_user
from todolist.views import logout_user 
from todolist.views import create
from todolist.views import show_json
from todolist.views import add
from todolist.views import change_status

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create, name='create-task'),
    path('json/', show_json, name='json'),
    path('add/', add, name='add'),
    path('change-status/<id>', change_status, name='change-status'),
]