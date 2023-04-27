from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm
from django.contrib.auth.decorators import login_required

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'forum_app/send_message.html', {'form': form})

@login_required
def inbox(request):
    messages = Message.objects.filter(receiver=request.user)
    return render(request, 'forum_app/message.html', {'messages': messages})
