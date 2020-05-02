from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
import random
from .send_sms import Sendsms
from .send_email import  SendEmail
from .forms import TodoForm,FeebackForm

from .models import Todo,Feedback
from django.contrib.auth.decorators import login_required
import  time
# Create your views here.


def home(request):

    if request.user.is_authenticated:
        return redirect('sucess')
    else:
        quotes = ["“Concentrate all your thoughts upon the work in hand. The sun's rays do not burn until brought to a focus.” -Alexander Graham Bell", "“Either you run the day or the day runs you.”-Jim Rohn",
                  "“I’m a greater believer in luck, and I find the harder I work the more I have of it.”-Thomas Jefferson", "“When we strive to become better than we are, everything around us becomes better too.” -Paulo Coelho"]
        a = random.randint(0, 3)

        return render(request, 'todo/home.html', {'quotes': quotes[a]})


def signupuser(request):
    if request.user.is_authenticated:
        return redirect('sucess')
    else:
        if (request.method == 'POST'):
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 == password2:
                try:
                    user = User.objects.create_user(
                        username=username, email=email, password=password1)
                    user.save()
                   
                    return redirect('loginuser')
                    # return HttpResponse("content")
                except IntegrityError:
                    return render(request, 'todo/signup.html', {'error': 'Unique Username Is required'})

            else:
                return render(request, 'todo/signup.html', {'error': 'Password Mismatch'})

            # return HttpResponse("content")
        else:

            return render(request, 'todo/signup.html')


def loginuser(request):
    if request.user.is_authenticated:
        return redirect('sucess')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, password=password, username=username)
            if user is not None:
                login(request, user)
                return redirect('sucess')
                # return HttpResponse("content")
            else:
                return render(request, 'todo/login.html', {'error': 'Username and Password Not Matched'})
        else:
            return render(request, 'todo/login.html')


@login_required()
def sucess(request):

    todos = Todo.objects.filter(user=request.user, completed=False)
    print(todos)
    context = {
        'todos': todos
    }
    return render(request, 'todo/todocreate.html', context)


@login_required()
def logoutuser(request):
    logout(request)
    return redirect('loginuser')

# Noy using form method
# def add(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         details = request.POST['details']
#         person = request.user
    # Todo.objects.create(title=title, detail=details, user=person)
#         redirect('sucess')
#     return render(request, 'todo/add.html')


@login_required()
def add(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            created_db_but_empty = form.save(commit=False)
            created_db_but_empty.user = request.user

            created_db_but_empty.save()
            return redirect('sucess')

    context = {
        'forms': TodoForm()
    }
    return render(request, 'todo/add.html', context)


@login_required()
def update(request, id):
    # todos = Todo.objects.get(pk=id) not error handing
    todos = get_object_or_404(Todo, pk=id)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todos)
        form.save()

        return redirect('sucess')
    else:
        form = TodoForm(instance=todos)
        context = {'forms': form}
        return render(request, 'todo/update.html', context)


@login_required()
def delete(request, id):
    delete_todo = Todo.objects.filter(pk=id)
    delete_todo.delete()
    return redirect('sucess')


@login_required()
def complete(request, id):
    todos = Todo.objects.get(pk=id)

    todos.completed = True
    todos.save()
    print(todos.completed)
    context = {
        "todos": todos
    }
    return redirect('sucess')


@login_required()
def completelist(request):
    todos = Todo.objects.filter(user=request.user, completed=True)
    return render(request, 'todo/complete.html', {'todos': todos})

@login_required()
def Feedback(request):
    if request.method=='POST':
        form=FeebackForm(request.POST)
        if form.is_valid():
            creted_db_wihtout_saving=form.save(commit=False)
            creted_db_wihtout_saving.user=request.user
            User.feedback.email=request.POST['email']
            
            creted_db_wihtout_saving.save()
            
            message__owner="--Username--"+request.user.username+"--Email--"+request.POST['email']+"--Feedback-- "+request.POST['feeds']
            message__user=request.user.username.capitalize() +",  Thank You For Your Support. "+"#StayHome"
            SendEmail(request.POST['email'],message__user)
            # Sendsms(message__owner)
            
            
            return redirect('sucess')
    else:
        form=FeebackForm(initial={'email':request.user.email})

        context={
            "message":'Please Enter Valid Email Address.',
            'form':form
        }
        return render(request, 'todo/Feedback.html',context)