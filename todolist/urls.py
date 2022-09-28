from turtle import update
from django.urls import path
from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_todolist
from todolist.views import delete_todolist
from todolist.views import update_todolist

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/',register, name='register'),
    path('login/',login_user,name='login'),
    path('logout/',logout_user,name='logout'),
    path('create-task',create_todolist,name='create_todolist'),
    path('delete-task/<int:id>',delete_todolist,name='delete_todolist'),
    path('update-task/<int:id>',update_todolist,name='update_todolist'),
]