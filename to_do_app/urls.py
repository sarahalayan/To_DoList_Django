"""
URL configuration for to_do_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from to_do import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',user_views.register,name='home+register'),
    path('register/',user_views.register,name='home+register'),
    path('addtask',views.TaskCreateView.as_view(template_name='to_do/addtask.html'),name='addtask'),
    path('login/',
         auth_views.LoginView.as_view(template_name='users/login.html'), 
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='users/logout.html'),
           name='logout'),
    path('profile/',user_views.myprofile, name='myprofile'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
           name='password_reset'),
    path('password-reset/done',
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), 
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), 
        name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
           name='password_reset_complete'),
   path('index/', views.task_list, name='index'),
    path('task/<int:pk>/delete/',views.TaskDeleteView.as_view(template_name='to_do/deletetask.html'),name='deletetask'),
    path('task/<int:pk>/edit/',views.TaskModifyView.as_view(template_name='to_do/edittask.html'),name='edittask'),
    path('task/<int:pk>/update/',views.TaskUpdateView.as_view(template_name='to_do/updatetask.html'),name='updatetask'),
    path('tasklist/',views.TaskListView.as_view(template_name='to_do/my_todo_list.html'),name='todo-list'),

]
