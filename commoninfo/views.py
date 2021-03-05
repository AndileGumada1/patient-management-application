from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from commoninfo.models import UserInfo



def addUserInfo(request):

    if request.method == "POST":
         username = request.POST['username']
         email = request.POST['email']
         password1 = request.POST['password1']
         password2 = request.POST['password2']
         firstname = request.POST['firstname']
         lastname = request.POST['lastname']
         unique_id = request.POST['unique_id']
         dateOfBirth = request.POST['dateOfBirth']
         user = UserInfo.objects.create_user(username = username, password = password1, email =email, firstname = firstname, lastname = lastname, unique_id = unique_id, dateOfBirth=dateOfBirth)
         user.save()
         print("user created")
         return redirect('/')
         messages.success(request, 'successfully added! .')

    else:
        return render(request, 'commoninfo/register.html')

def fetchUserInfo(request):

    context = {
    'object' : obj
    'username': obj.username,
    'unique_id': obj.unique_id,
    'dateOfBirth': obj.dateOfBirth
 
    }
    return render(request, 'commoninfo/fetch.html', context)


def commoninfo(request):
    return render(request, 'commoninfo/base.html')
