from django.shortcuts import render
from forum_app import forms

from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Feedback

def index(request):
    post = forms.PostBeitrag()
    welcome = request.user.username

    if request.method == 'POST':
        post = forms.PostBeitrag(request.POST)

        if post.is_valid():
            post.save(commit=True)
            post = forms.PostBeitrag()
            return HttpResponseRedirect(reverse('index'))
        
    return render(request, 'forum_app/index.html',{'beitrag_form':post, 'username':welcome})



def lehrer(request):
    all_feedback = Feedback.objects.all()
    if request.method == 'POST':
            title = request.POST['title']
            content = request.POST['content']
            feedback = Feedback(title=title, content=content)
            feedback.save()
		    
    return render(request, 'forum_app/lehrer.html', {'feedback': all_feedback})

def rules(request):
    return render(request,"forum_app/rules.html")
    
