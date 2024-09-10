from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib.auth.decorators import login_required




@login_required(login_url='/')
def homepage_fun(request):

    return render(request,'index.html')

@login_required(login_url='/')
def getvalue_fun(request,id): 
    context = {
         'id' : id
    }

    return render(request,'input.html',context)


@login_required(login_url='/')
def temp_1(request):

    if request.method == 'POST':
         
          education = request.POST['education']
          school = request.POST['school']
          yearstart = request.POST['yearstart']
          yearend = request.POST['yearend']

          education1 = request.POST['education1']
          school1 = request.POST['school1']
          yearstart1 = request.POST['yearstart1']
          yearend1 = request.POST['yearend1']

          project =  request.POST['project']
          techonology = request.POST['technology']
          point1 = request.POST['point1']
          point2 = request.POST['point2']
          point3 = request.POST['point3']

          project1 =  request.POST['project1']
          techonology1 = request.POST['technology1']
          point11 = request.POST['point11']
          point21 = request.POST['point21']
          point31 = request.POST['point31']

          role = request.POST['role']
          about_role = request.POST['about_role']
          name = request.POST['name']
          phone = request.POST['phone']
          mail = request.POST['mail']
          address = request.POST['address']
          summary = request.POST['summary']
          skill = request.POST['skill']
          sk = skill.split(',')
          language = request.POST['language']
          lan = language.split(',')

          context = {
               'education' : education,
               'school' : school,
               'yearstart' : yearstart,
               "yearend" : yearend,

               'education1' : education1,
               'school1' : school1,
               'yearstart1' : yearstart1,
               "yearend1" : yearend1,

               'project' :project,
               'technology':techonology,
               'point1':point1,
               'point2':point2,
               'point3':point3,

               'project1' :project1,
               'technology1':techonology1,
               'point11':point11,
               'point21':point21,
               'point31':point31,

               
               'role' : role,
               'about_role' : about_role,
               'name' : name,
               'phone' : phone,
               'mail' : mail,
               'address' : address,
               'summary' : summary,
               'skill' : sk,
               'language' : lan          
          }
          
     
          return render(request,'resume1.html',context)
    
@login_required(login_url='/')
def temp_2(request):

     if request.method == 'POST':
         
          education = request.POST['education']
          school = request.POST['school']
          yearstart = request.POST['yearstart']
          yearend = request.POST['yearend']

          education1 = request.POST['education1']
          school1 = request.POST['school1']
          yearstart1 = request.POST['yearstart1']
          yearend1 = request.POST['yearend1']

          project =  request.POST['project']
          techonology = request.POST['technology']
          point1 = request.POST['point1']
          point2 = request.POST['point2']
          point3 = request.POST['point3']

          project1 =  request.POST['project1']
          techonology1 = request.POST['technology1']
          point11 = request.POST['point11']
          point21 = request.POST['point21']
          point31 = request.POST['point31']

          role = request.POST['role']
          about_role = request.POST['about_role']
          name = request.POST['name']
          phone = request.POST['phone']
          mail = request.POST['mail']
          address = request.POST['address']
          summary = request.POST['summary']
          skill = request.POST['skill']
          sk = skill.split(',')
          language = request.POST['language']
          lan = language.split(',')

          context = {
               'education' : education,
               'school' : school,
               'yearstart' : yearstart,
               "yearend" : yearend,

               'education1' : education1,
               'school1' : school1,
               'yearstart1' : yearstart1,
               "yearend1" : yearend1,

               'project' :project,
               'technology':techonology,
               'point1':point1,
               'point2':point2,
               'point3':point3,

               'project1' :project1,
               'technology1':techonology1,
               'point11':point11,
               'point21':point21,
               'point31':point31,

               
               'role' : role,
               'about_role' : about_role,
               'name' : name,
               'phone' : phone,
               'mail' : mail,
               'address' : address,
               'summary' : summary,
               'skill' : sk,
               'language' : lan          
          }
     
          return render(request,'resume2.html',context)
     
@login_required(login_url='/')
def temp_3(request):
          
     if request.method == 'POST':
         
          education = request.POST['education']
          school = request.POST['school']
          yearstart = request.POST['yearstart']
          yearend = request.POST['yearend']

          education1 = request.POST['education1']
          school1 = request.POST['school1']
          yearstart1 = request.POST['yearstart1']
          yearend1 = request.POST['yearend1']

          project =  request.POST['project']
          techonology = request.POST['technology']
          point1 = request.POST['point1']
          point2 = request.POST['point2']
          point3 = request.POST['point3']

          project1 =  request.POST['project1']
          techonology1 = request.POST['technology1']
          point11 = request.POST['point11']
          point21 = request.POST['point21']
          point31 = request.POST['point31']

          role = request.POST['role']
          about_role = request.POST['about_role']
          name = request.POST['name']
          phone = request.POST['phone']
          mail = request.POST['mail']
          address = request.POST['address']
          summary = request.POST['summary']
          skill = request.POST['skill']
          sk = skill.split(',')
          language = request.POST['language']
          lan = language.split(',')

          context = {
               'education' : education,
               'school' : school,
               'yearstart' : yearstart,
               "yearend" : yearend,

               'education1' : education1,
               'school1' : school1,
               'yearstart1' : yearstart1,
               "yearend1" : yearend1,

               'project' :project,
               'technology':techonology,
               'point1':point1,
               'point2':point2,
               'point3':point3,

               'project1' :project1,
               'technology1':techonology1,
               'point11':point11,
               'point21':point21,
               'point31':point31,

               
               'role' : role,
               'about_role' : about_role,
               'name' : name,
               'phone' : phone,
               'mail' : mail,
               'address' : address,
               'summary' : summary,
               'skill' : sk,
               'language' : lan          
          }
     
          return render(request,'resume3.html',context)

@login_required(login_url='/')
def temp_4(request):
     
     if request.method == 'POST':
         
          education = request.POST['education']
          school = request.POST['school']
          yearstart = request.POST['yearstart']
          yearend = request.POST['yearend']

          education1 = request.POST['education1']
          school1 = request.POST['school1']
          yearstart1 = request.POST['yearstart1']
          yearend1 = request.POST['yearend1']

          project =  request.POST['project']
          techonology = request.POST['technology']
          point1 = request.POST['point1']
          point2 = request.POST['point2']
          point3 = request.POST['point3']

          project1 =  request.POST['project1']
          techonology1 = request.POST['technology1']
          point11 = request.POST['point11']
          point21 = request.POST['point21']
          point31 = request.POST['point31']

          role = request.POST['role']
          about_role = request.POST['about_role']
          name = request.POST['name']
          phone = request.POST['phone']
          mail = request.POST['mail']
          address = request.POST['address']
          summary = request.POST['summary']
          skill = request.POST['skill']
          sk = skill.split(',')
          language = request.POST['language']
          lan = language.split(',')

          context = {
               'education' : education,
               'school' : school,
               'yearstart' : yearstart,
               "yearend" : yearend,

               'education1' : education1,
               'school1' : school1,
               'yearstart1' : yearstart1,
               "yearend1" : yearend1,

               'project' :project,
               'technology':techonology,
               'point1':point1,
               'point2':point2,
               'point3':point3,

               'project1' :project1,
               'technology1':techonology1,
               'point11':point11,
               'point21':point21,
               'point31':point31,

               
               'role' : role,
               'about_role' : about_role,
               'name' : name,
               'phone' : phone,
               'mail' : mail,
               'address' : address,
               'summary' : summary,
               'skill' : sk,
               'language' : lan          
          }
          return render(request,'resume4.html',context)

@login_required(login_url='/')
def temp_5(request):
     if request.method == 'POST':
         
          education = request.POST['education']
          school = request.POST['school']
          yearstart = request.POST['yearstart']
          yearend = request.POST['yearend']

          education1 = request.POST['education1']
          school1 = request.POST['school1']
          yearstart1 = request.POST['yearstart1']
          yearend1 = request.POST['yearend1']

          project =  request.POST['project']
          techonology = request.POST['technology']
          point1 = request.POST['point1']
          point2 = request.POST['point2']
          point3 = request.POST['point3']

          project1 =  request.POST['project1']
          techonology1 = request.POST['technology1']
          point11 = request.POST['point11']
          point21 = request.POST['point21']
          point31 = request.POST['point31']

          role = request.POST['role']
          about_role = request.POST['about_role']
          name = request.POST['name']
          phone = request.POST['phone']
          mail = request.POST['mail']
          address = request.POST['address']
          summary = request.POST['summary']
          skill = request.POST['skill']
          sk = skill.split(',')
          language = request.POST['language']
          lan = language.split(',')

          context = {
               'education' : education,
               'school' : school,
               'yearstart' : yearstart,
               "yearend" : yearend,

               'education1' : education1,
               'school1' : school1,
               'yearstart1' : yearstart1,
               "yearend1" : yearend1,

               'project' :project,
               'technology':techonology,
               'point1':point1,
               'point2':point2,
               'point3':point3,

               'project1' :project1,
               'technology1':techonology1,
               'point11':point11,
               'point21':point21,
               'point31':point31,

               
               'role' : role,
               'about_role' : about_role,
               'name' : name,
               'phone' : phone,
               'mail' : mail,
               'address' : address,
               'summary' : summary,
               'skill' : sk,
               'language' : lan          
          }
          return render(request,'resume5.html')




    


  