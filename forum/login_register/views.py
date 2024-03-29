from django.shortcuts import render
from login_register import forms

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



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

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            
            else:
                HttpResponse('Account not active')
        else:
            HttpResponse('Falsche Anmeldedaten')
    else:
        return render(request,'forum_app/login.html')
    
    return render(request,'forum_app/login.html')
