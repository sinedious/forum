from django.shortcuts import render, redirect
from profil.forms import userProfileForm
from django.contrib.auth.decorators import login_required


@login_required
def changeData(request):
    user = request.user    
    if request.method == 'POST':
        form = userProfileForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect('profil')
    else:
        form = userProfileForm(instance=user)

    return render(request,'forum_app/profil.html', {'profil':form})

    
