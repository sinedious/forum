from django.shortcuts import render

def index(request):
    return render(request, 'forum_app/index.html')

def login(request):
    return render(request, 'forum_app/login.html')
