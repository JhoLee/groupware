from django.shortcuts import render
from . import dao


def index(request):
    posts = dao.selectTest()
    return render(request, 'mysqlTest.html', {'posts': posts})
