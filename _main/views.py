from django.shortcuts import render
from . import dao


def index(request):
    posts = dao.selectTest()
    return render(request, 'mysqlTest.html', {'posts': posts})


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'registration/login.html')


def logout(request):
    return render(request, 'registration/logout.html')
