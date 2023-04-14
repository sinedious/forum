from django.shortcuts import render
from forum_app import forms

def index(request):
    post = forms.PostBeitrag()

    if request.method == 'POST':
        post = forms.PostBeitrag(request.POST)

        if post.is_valid():
            post.save(commit=True)
            post = forms.PostBeitrag()
            return render(request, 'forum_app/index.html',{'beitrag_form':post})
        
    return render(request, 'forum_app/index.html',{'beitrag_form':post})




def login(request):
    login = forms.User_Login()

    if request.method == 'POST':
        login = forms.User_Login(request.POST)

        if login.is_valid():
            print('Login Succses')


    return render(request, 'forum_app/login.html',{'login':login})

def register(request):

    registered = False

    if request.method == 'POST':
        register = forms.register_form(request.POST)

        if register.is_valid():
            user = register.save()
            user.set_password(user.password)
            user.save()

            registered=True

    else:
        register = forms.register_form()

    return render(request, 'forum_app/register.html', {'register_form': register, 'registered':registered})
