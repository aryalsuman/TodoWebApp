"""Todo_web_application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from todo import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signupuser, name='signupuser'),
    path('', views.home, name='home'),
    path('login/', views.loginuser, name='loginuser'),
    path('todo/', views.sucess, name='sucess'),
    path('add/', views.add, name='add'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('complete/<int:id>', views.complete, name='complete'),
    path('completelist/', views.completelist, name='completelist'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('feedback/', views.Feedback, name='feedback'),
]
