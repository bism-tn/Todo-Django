"""
URL configuration for Todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from taskmanager.views import UserresgisterView
from taskmanager.views import LoginView,TaskAddView,TaskdeleteView,TaskDetailView,TaskupdateView
from taskmanager.views import TaskcompleteView,TaskreadView,Signout,Userdetails
urlpatterns = [
    path('admin/', admin.site.urls),
    path('taskmanager/signup/',UserresgisterView.as_view(),name="signup"),
    path('taskmanager/login/',LoginView.as_view(),name="login"),
    path('taskmanager/addTask/',TaskAddView.as_view(),name="addtask"),
    path('taskmanager/readtask/',TaskreadView.as_view(),name="all_task"),
    path("taskmanager/delete/<int:pk>",TaskdeleteView.as_view(),name="delete"),
    path("taskmanager/details/<int:pk>",TaskDetailView.as_view(),name="details"),
    path("taskmanager/update/<int:pk>",TaskupdateView.as_view(),name="update"),
    path('taskmanager/signout',Signout.as_view(),name="signout"),
    path('taskmanager/complete/<int:pk>',TaskcompleteView.as_view(),name="complete"),
    path('taskmanager/home',Userdetails.as_view(),name="Home"),
    # path('taskmanager/home',HomeView.as_view(),name="home")
    ]   
