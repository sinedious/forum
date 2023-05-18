from django.http import HttpResponseRedirect
from django.urls import reverse



from typing import Any, Dict
from django.shortcuts import render, redirect, reverse, get_object_or_404
from forum_app import forms
from .models  import beitrag, comment
from django.views.generic.detail import DetailView
from .forms import CommentForm



def index(request):
    post = forms.PostBeitrag()
    all_beitrag = beitrag.objects.all()
    all_comment = comment.objects.all()


    if request.method == 'POST':
        post = forms.PostBeitrag(request.POST)

        if post.is_valid():
            post.save(commit=True)
            post = forms.PostBeitrag()
            return HttpResponseRedirect(reverse('index'))
        
    return render(request, 'forum_app/index.html',{'beitrag_form':post, 'beitrag':all_beitrag, 'beitrag.comment.all':all_comment,})




class BeitragDetail(DetailView):
    model = beitrag
    template_name = 'forum_app/beitrag_details.html'
    pk_field = 'pk'
    pk_url_kwarg = 'pk'
    count_hit = True

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            comment = form.save(commit=False)  
            comment.author = request.user
            comment.beitrag = post
            comment.save()  
            return redirect('beitrag-detail', pk=post.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    


def like_beitrag(request, pk):
    Beitrag = get_object_or_404(beitrag, pk=pk)
    if request.user.is_authenticated:
        if request.user in Beitrag.likes.all():
            Beitrag.likes.remove(request.user)
        else:
            Beitrag.likes.add(request.user)
    return redirect('beitrag-detail', pk=pk)




    
