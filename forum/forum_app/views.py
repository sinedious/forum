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
