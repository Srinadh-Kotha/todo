from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('insertrecord',views.insertrecord,name='insertrecord'),
    path('logindata',views.logindata,name='logindata'),
    path('logout',views.logout,name='logout'),
    path('forgotpass',views.forgotpass,name='forgotpass'),
    path('forgotPassword',views.forgotPassword,name='forgotPassword'),
    path('passSent',views.passSent,name='passSent'),
    path('addtodolist',views.addtodolist,name='addtodolist'),
    path('todo_listadd',views.todo_listadd,name='todo_listadd'),
    path('my_todo',views.my_todo,name='my_todo'),
    # path('todolist',views.todolist,name='todolist'),
    path('del_todo/<int:i>/',views.del_todo,name='del_todo'),


]