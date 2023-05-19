from django.shortcuts import render
from teacherdashboard.models import ProjectEvents,ProjectEventEntry
from account.models import profile
# Create your views here.
def Dashboard(request):
    return render(request, 'tdashboard/dashboardui.html')

def Events(request):
    if request.session.get('user_email'):
        ProjectEv=ProjectEvents.objects.all().values()
        context={
            'ProjectEv':ProjectEv,
        }
        # if request.method == 'POST':
        #     user_name=request.session.get('username')
        #     profile_data=profile.objects.get(username=user_name)
        #     pro_id=request.POST.get('projecteid')
        #     # print("****************:",pro_id)

        #     ProjectEv=ProjectEvents.objects.get(peid=pro_id)
        #     print(ProjectEv)
        #     Project_entry=ProjectEventEntry.objects.create(peinfo=ProjectEv,userinfo=profile_data)
            
        return render(request, 'tdashboard/events.html',context)
    else:
        return render(request, 'account/login.html')