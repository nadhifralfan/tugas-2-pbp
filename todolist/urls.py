from django.urls import path
from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_todolist
from todolist.views import delete_todolist
from todolist.views import update_todolist
from todolist.views import show_todolist_json
from todolist.views import add_todolist
from todolist.views import show_todolist_ajax
from todolist.views import update_todolist_ajax
from todolist.views import delete_todolist_ajax

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/',register, name='register'),
    path('login/',login_user,name='login'),
    path('logout/',logout_user,name='logout'),
    path('create-task',create_todolist,name='create_todolist'),
    path('delete-task/<int:id>',delete_todolist,name='delete_todolist'),
    path('update-task/<int:id>',update_todolist,name='update_todolist'),
    path('json/',show_todolist_json, name='show_todolist_json'),
    path('add-task/', add_todolist, name='add_todolist'),
    path('ajax/',show_todolist_ajax, name='show_todolist_ajax'),
    path('update-task-ajax/<int:id>',update_todolist_ajax,name='update_todolist_ajax'),
    path('delete-task-ajax/<int:id>',delete_todolist,name='delete_todolist_ajax'),
]