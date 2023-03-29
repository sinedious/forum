from django.shortcuts import render
from second_try.models import AccessRecord,Topic,Webpage,Users_test


# Create your views here.

def main(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,"index.html",context=date_dict)

def login(request):
    return render(request,"login.html")

def user(request):
    user_list = Users_test.objects.all()
    user_dict = {'user_register':user_list}
    return render(request,'user.html',context=user_dict)

