from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from ProjectCommunity import settings
from django.contrib.auth import authenticate, login, logout
# from . tokens import generate_token
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from projects.models import uploadProject
from projects.models import collegeList,Courses
from account.models import profile
# from array import array
# Create your views here.

# Create your views here.
def allProject(request):
    if request.session.get('user_email'):
        # print (user.id)
        uploadproject=uploadProject.objects.all().values().order_by('-pid')
        # uploadproject=uploadproject.reverse()
        mailid=request.session.get('username')
        temp_profile=profile.objects.values('profilePic').filter(username=mailid)
        result=temp_profile.values('profilePic').first()
        profilePicpath = result['profilePic']
        context = {
             "uploadproject": uploadproject,
             "user_email":request.session.get('user_email'),   
             "isteacher":request.session.get('isteacher'),
             "navprofile":profilePicpath,
        }
        return render(request, "pdashboard/allproject.html",context)
    else:
        return render(request, 'account/login.html')

def college_List(request):
    if request.session.get('user_email'):
        # print (user.id)
        collegelist=collegeList.objects.all().values()
        mailid=request.session.get('username')
        temp_profile=profile.objects.values('profilePic').filter(username=mailid)
        result=temp_profile.values('profilePic').first()
        profilePicpath = result['profilePic']
        context = {
             "colleges": collegelist,
             "user_email":request.session.get('user_email'),  
            "isteacher":request.session.get('isteacher'),  
            "navprofile":profilePicpath,
        }
        return render(request, "pdashboard/collegeList.html",context)
    else:
        return render(request, 'account/login.html')
 

def Upload(request):
    collegelist=collegeList.objects.all().values()
    course=Courses.objects.all().values()
    mailid=request.session.get('username')
    temp_profile=profile.objects.values('profilePic').filter(username=mailid)
    result=temp_profile.values('profilePic').first()
    profilePicpath = result['profilePic']
    context = {
             "colleges": collegelist,
             "course":course,
             "user_email":request.session.get('user_email'),   
             "isteacher":request.session.get('isteacher'),
             "navprofile":profilePicpath
    }
    if request.method == 'POST':
        zipfile = request.FILES["zipfile"]
        outputss = request.FILES["screenshot"]
       
        user_name=request.session.get('username')
        firstname=request.session.get('fname')
        lastname=request.session.get('lname')
        emailid=request.session.get('user_email')
        
        tagsword=request.POST.get('tags[]')
        
        tagsword=tagsword.lower()
        print(tagsword)
        projectfile=uploadProject.objects.create(username=user_name,fname=firstname,lname=lastname,email=emailid,College=request.POST.get('college'),course=request.POST.get('branch'),projectname=request.POST.get('projectname'),tags=tagsword,description=request.POST.get('description'),zip_project=zipfile,outputSS=outputss)
        
        projectfile.save()
    
        return render(request, "pdashboard/upload.html",{"uploadsuccess":"Upload successful!","user_email":request.session.get('user_email')})
    if request.session.get('user_email'):
        # print (user.id)
        return render(request, "pdashboard/upload.html",context)
    else:
        return render(request, 'account/login.html')
    
def treandingProject(request):
    # print (user.id)
    if request.session.get('user_email'):
        
        if request.method == 'POST':
            current_user = request.user
            # print(current_user)
        
            user_name=request.session.get('username')
            profile_data=profile.objects.get(username=user_name)
            upload_project=uploadProject.objects.all().values()
            context={"upload_project":upload_project}
            answers_list = list(context['upload_project'])
            tags_list = []
            projectname_list = []
            pid_list = []
            outputSS_list=[]
            zip_project_list=[]
            
            # zipfile = request.FILES["zipfile"]
            fkey=request.POST.get('titlekeyword')
            print(fkey)
            fkey=fkey.lower()
            for item in answers_list:
                tags = item.get('tags')
                if tags:
                    tags_list.extend(tags.split(','))
                
                    if fkey in tags_list:
                        pid_list.append(item.get('pid'))
                        projectname_list.append(item.get('projectname'))
                        outputSS_list.append(item.get('outputSS'))
                        zip_project_list.append(item.get('zip_project'))
                    
            # print(tags_list)
            # print(pid_list)
            # print(projectname_list)
            # print(outputSS_list)
            # print(zip_project_list)
            
            cuser = uploadProject.objects.filter(pid__in=pid_list)
            # print(c)
            mailid=request.session.get('username')
            temp_profile=profile.objects.values('profilePic').filter(username=mailid)
            result=temp_profile.values('profilePic').first()
            profilePicpath = result['profilePic']
            context={
                "user_email":request.session.get('user_email'),"current_user":current_user,
                "profile_data":profile_data,
                "upload_project":upload_project,
                "isteacher":request.session.get('isteacher'),
                "cuser":cuser,
                "navprofile":profilePicpath,
                # "tags_list":tags_list,
                # "projectname_list":projectname_list,
                # "pid_list":pid_list,
                # "outputSS_list":outputSS_list,
                # "zip_project_list":zip_project_list,
                # "tags_list":tags_list        
            }
            return render(request, "pdashboard/treandingprojects.html",context)
        
            context={
                "user_email":request.session.get('user_email'),"current_user":current_user,
                "profile_data":profile_data,
                "upload_project":upload_project,
                "isteacher":request.session.get('isteacher')}
        return render(request, "pdashboard/treandingprojects.html",context)
    else:
        return render(request, 'account/login.html')

def aboutUs(request):
    if request.session.get('user_email'):
        user_name=request.session.get('username')
        profile_data=profile.objects.get(username=user_name)
        upload_project=uploadProject.objects.all().values()
        context={"upload_project":upload_project}
        mailid=request.session.get('username')
        temp_profile=profile.objects.values('profilePic').filter(username=mailid)
        result=temp_profile.values('profilePic').first()
        profilePicpath = result['profilePic']
        context={
            "user_email":request.session.get('user_email'),
            "profile_data":profile_data,
            "isteacher":request.session.get('isteacher'),
            "navprofile":profilePicpath,}
        return render(request, "pdashboard/aboutus.html",context)
    else:
        return render(request, "pdashboard/aboutus.html")
        