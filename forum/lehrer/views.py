from django.shortcuts import render
from .models import Feedback

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
