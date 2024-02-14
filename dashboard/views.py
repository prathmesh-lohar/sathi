from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app1.models import profile,media
from extra.models import income,experience,Qualification,color,work,hobbies,height
from dashboard.forms import profileForm

# Create your views here.

def dashboard(request):
    if request.user.is_superuser:
        return render(request, "dashboard/index.html")
        
    else:
        return redirect('/dashboard/login')

def login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        user = auth.authenticate(username=username, password=password)
            
        if user is not None:
            auth.login(request, user)
            if request.user.is_superuser:
                return redirect('/dashboard')
            else:
                messages.error(request, "You are not a staff member")

        else:
            messages.error(request, "Invalid Username And Password")
            # return HttpResponse("uname , password invalid ")
    
    return render(request, "dashboard/auth-login-basic.html")

def logout(request):
    auth.logout(request)

    return redirect('/dashboard/login')


@login_required(login_url='/dashboard/login')

def all_staff(request):
    users = User.objects.filter(is_staff=True)
    
    data = {
        'users':users,
    }
    
    return  render(request,"dashboard/all_staff.html",data)
 


@login_required(login_url='/dashboard/login')
def staff(request,username):
    
    profiles = profile.objects.filter(related_officer=username)
    
  
    
    data = {
        'profiles':profiles
    }
     
    return render(request, "dashboard/profiles.html",data)



@login_required(login_url='/dashboard/login')

def alter_user(request,username):
    from extra.models import income,experience,Qualification,color,work,hobbies,height
    
    
    user = User.objects.filter(username=username).first()
    id = user.id
    
    profiler = profile.objects.filter(user=id).first()

    incomelist = income.objects.all()
    
    
    colorlist = color.objects.all()
    
    Qualificationlist= Qualification.objects.all()
    worklist= work.objects.all()
    experiencelist = experience.objects.all()
    hobbieslist = hobbies.objects.all()
    heightlist = height.objects.all()
    
    
    if request.method == "POST":
            mobile = request.POST.get('mobile')
            mstatus = request.POST.get('mstatus')
            dob = request.POST.get('dob')
            height = request.POST.get('height')
            color = request.POST.get('color')
            qualification = request.POST.get('tags')
            work = request.POST.get('work')
            experience = request.POST.get('experience')
            Hobbies = request.POST.get('hobie')
            Income = request.POST.get('Income')
            medical_condition = request.POST.get('medical_condition')
            city = request.POST.get('city')
            about = request.POST.get('about')
            userid = request.POST.get('userid')
            gender = request.POST.get('gender')
            uid = request.POST.get('uid')
            regofor = request.POST.get('regofor')


            father_name = request.POST.get('father_name')
            father_education = request.POST.get('father_education')
            father_occupation = request.POST.get('father_occupation')
            mother_name = request.POST.get('mother_name')
            mother_education = request.POST.get('mother_education')
            mother_occupation = request.POST.get('mother_occupation')
            sister = request.POST.get('sister')
            brother = request.POST.get('brother')
            native_place = request.POST.get('native_place')
            relatives = request.POST.get('relatives')

            username = request.POST.get('username')
            id = request.POST.get('id')

            verify = request.POST.get('verify')
            
            vstatus = False
            
            if verify == "on":
                vstatus=True
        
            if profile.objects.filter(username=username).exists():
                obj=profile.objects.filter(username=uid).update(user=id,mobile=mobile,marrital_status=mstatus,dob=dob,height=height,color=color,Qualification=qualification,work=work,experience=experience,hobbies=Hobbies,income=Income,medical_condition=medical_condition,city=city,about_me=about,gender=gender,registerfor=regofor,is_approved=vstatus)
               
                messages.success(request, "details uploaded successfully")
                
            
            else:
                # user = User.objects.filter(id=uid).first()
                obj=profile(username=uid,mobile=mobile,marrital_status=mstatus,dob=dob,height=height,color=color,Qualification=qualification,work=work,experience=experience,hobbies=Hobbies,income=Income,medical_condition=medical_condition,city=city,about_me=about,gender=gender,registerfor=regofor,is_approved=vstatus)
                obj.save()
                messages.success(request, "details uploaded successfully")
                
                # obj2.save()
            return redirect('/dashboard/all_staff')
        
    data = {
        'profiler':profiler,
        'incomelist':incomelist,
        'heightlist':heightlist,
        'colorlist':colorlist,
        'Qualificationlist':Qualificationlist,
        'worklist':worklist,
        'experiencelist':experiencelist,
        'hobbieslist':hobbieslist,
        
    }
    return render(request, "dashboard/alter_user.html",data)