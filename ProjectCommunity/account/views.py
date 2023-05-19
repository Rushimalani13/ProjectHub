from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from ProjectCommunity import settings
from django.contrib.auth import authenticate, login, logout
# from . tokens import generate_token
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

# from django.contrib.auth.decorators import login_required
from account.models import profile
from projects.models import uploadProject
from account.models import teacherProfile
from projects.models import TreandingProjects
# Create your views here.

def home(request): 
    tp=TreandingProjects.objects.all().values()
    mailid=request.session.get('username')
    temp_profile=profile.objects.values('profilePic').filter(username=mailid)
    result=temp_profile.values('profilePic').first()
    # profilePicpath = result['profilePic']
    context = {
            "tp": tp,
            "user_email":request.session.get('user_email'),  
            "isteacher":request.session.get('isteacher'),          
            # "navprofile":profilePicpath,
        }   
    return render(request, "pdashboard/index.html",context)

def Profile(request):
    mailid=request.session.get('username')
    temp_profile=profile.objects.values('profilePic').filter(username=mailid)
    result=temp_profile.values('profilePic').first()
    profilePicpath = result['profilePic']
    tp=TreandingProjects.objects.all().values()
    current_user = request.user
    print(current_user)
    if request.session.get('user_email'):
        # print (user.id)
        user_name=request.session.get('username')
        profile_data=profile.objects.get(username=user_name)
        upload_project=uploadProject.objects.filter(username=user_name)
        
        #p_count = uploadProject.objects.filter(username='myname', status=0).count()
        
        return render(request, "account/profile.html",{"user_email":request.session.get('user_email'),"current_user":current_user,"profile_data":profile_data,"upload_project":upload_project,"isteacher":request.session.get('isteacher'),"tp": tp,"navprofile":profilePicpath})
    else:
        return render(request, "account/login.html")

def Login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
 
        user = authenticate(username=username, password=pass1)
        if  user is not None and user.is_staff==True:
            request.session['isteacher']=True
        
        if user is not None:
            tp=TreandingProjects.objects.all().values()
            login(request, user)
            fname = user.first_name
            lname = user.last_name
            request.session['username']=username
            request.session['fname'] = user.first_name
            request.session['lname'] = user.last_name
            request.session['use_id']=user.id
            request.session['user_email']=user.email
            
            profile_data=profile.objects.filter(username=username)
            mailid=request.session.get('username')
            temp_profile=profile.objects.values('profilePic').filter(username=mailid)
            result=temp_profile.values('profilePic').first()
            profilePicpath = result['profilePic']
            #messages.success(request, "Logged In Sucessfully!!")
            return render(request, "pdashboard/index.html",{"fname":fname,"user_email":request.session.get('user_email'),"isteacher":request.session.get('isteacher'),"tp": tp,"profile_data":profile_data,"navprofile":profilePicpath})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('login')
    
    return render(request, "account/login.html")



def Signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signup')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('signup')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('signup')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('signup')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False
        myuser.is_active = False
        myuser.save()
        profile_data=profile.objects.create(username=username,fname=fname,lname=lname,email=email,phone="",College="",course="",passyear="")
        
        profile_data.save()
        messages.success(request, "Your Account has been created succesfully!!")
        
        return redirect('login')
                
    return render(request, "account/signup.html")

def Logout(request):
    request.session.flush()
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('login')

def EditProfile(request):
    current_user = request.user
    if request.method == 'POST':
        user_name=request.session.get('username')
        firstname=request.session.get('fname')
        lastname=request.session.get('lname')
        emailid=request.session.get('user_email')
        outputss = request.FILES["profilepic"]
        
        profile_data=profile.objects.get(username=user_name)
        profile_data.phone=request.POST.get('pnumber')
        profile_data.College=request.POST.get('College')
        profile_data.course=request.POST.get('Course')
        profile_data.passyear=request.POST.get('Year')
        profile_data.profilePic=outputss
        
        profile_data.save()
        
        mailid=request.session.get('username')
        temp_profile=profile.objects.values('profilePic').filter(username=mailid)
        result=temp_profile.values('profilePic').first()
        profilePicpath = result['profilePic']    
        return render(request, "account/profile.html",{"user_email":request.session.get('user_email'),"current_user":current_user,"updatesuccess":"Update successfully!","profile_data":profile_data,"navprofile":profilePicpath})
    if request.session.get('user_email'):
        return render(request, "account/edit_profile.html",{"user_email":request.session.get('user_email'),"current_user":current_user})
    else:
        return render(request, "account/login.html")
    
def teacherSignup(request):
    if request.method == "POST":
        username = request.POST['uname']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['emailid']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('teachersignup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('teachersignup')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('teachersignup')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('teachersignup')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('teachersignup')
        
        myuser = User.objects.create_user(username, email, pass1,is_staff=True)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False
        myuser.is_active = True
        myuser.save()
        
        Mobileno = request.POST['Mobileno']
        College = request.POST['College']
        Course = request.POST['Course']
        id_proof = request.FILES["id_proof"]
        ppic = request.FILES["ppic"]
        teacher_data=teacherProfile.objects.create(username=username,fname=fname,lname=lname,email=email,phone=Mobileno,College=College,course=Course,idproof=id_proof,profilePic=ppic)
        
        teacher_data.save()
        messages.success(request, "Your Account has been created succesfully!!")
        
        return redirect('login')
                
    return render(request, "account/teacher_signup.html",{"isteacher":request.session.get('isteacher')})