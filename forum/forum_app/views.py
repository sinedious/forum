from django.shortcuts import render
from forum_app import forms

def index(request):
    return render(request, 'forum_app/index.html')

def login(request):
    login = forms.User_Login()

    if request.method == 'POST':
        login = forms.User_Login(request.POST)

        if login.is_valid():
            print('Login Succses')


    return render(request, 'forum_app/login.html',{'login':login})
