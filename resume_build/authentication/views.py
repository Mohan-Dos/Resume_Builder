from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.conf import settings
from .models import *

def landign_page_fun(request):
    
    return render(request,'landing_page.html')

def login_fun(request):

    if request.user.is_authenticated:

        return redirect('/resume/homepage/')

    if request.method == 'POST':

        username = request.POST['name']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        if user is not None:

            login(request,user)

            subject = 'Holder databse'
            message = f'hi {user.username} you are loggined in Resume builder'
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = [user.email]

            send_mail(subject,message,email_from,recipient_list)

            return redirect('homepage')
    
        else:
            
            context = {
                'error' : "* Invalid Username or password"
            }

            return render(request,'login.html',context)

    return render(request,'login.html')
    

def register_fun(request):

    if request.method == 'POST':

       print("register page")

       username = User.objects.filter(username = request.POST['name'])

       if len(username) > 0:
           
           context = {
               'error' : "* Username already exist"
           }

           return render(request,'register.html',context)
       
       else:
           
           username = request.POST['name']
           mail = request.POST['mail']

           new_user = User(username = username, email = mail)

           new_user.set_password(request.POST['password'])
           new_user.save()

           return redirect('/')
    
    return render(request,'register.html')


def logout_fun(request):

    del_user = request.user
    logout(request)
    del_user.delete()
    return redirect('/')




    
