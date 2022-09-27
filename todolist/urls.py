from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, addTask #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import change_status, delete_status

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', addTask, name='addTask'),
    path('change-status/', change_status, name='change_status'),
    path('delete-status/', delete_status, name='delete_status'),
]