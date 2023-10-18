from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app1.models import profile,family_details,media

# Create your views here.

@login_required(login_url='/staff/login')
def dashboard(request):
    officer = request.user.username
    # users = User.objects.all()[1:]
    users = profile.objects.filter(related_officer=officer).order_by('-id')
    count = users.count()

    data = {
        'users':users,
        'officer':officer,
        'count':count,
      
    }
    return render(request, "staff/dashboard.html",data)

def login(request):
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        user = auth.authenticate(username=username, password=password)
            
        if user is not None:
            auth.login(request, user)
            if request.user.is_staff:
                return redirect('/staff')
            else:
                messages.error(request, "You are not a staff member")

        else:
            messages.error(request, "Invalid Username And Password")
            # return HttpResponse("uname , password invalid ")

    return render(request, "staff/login.html")


@login_required(login_url='/staff/login')
def new_profile(request):
    return render(request,"staff/new_profile.html")


def logout(request):
    auth.logout(request)

    return redirect('/staff/login')

@login_required(login_url='/staff/login')
def upload_details(request,username):
    username=username
    details  = profile.objects.filter(username=username).first()
    fdetails  = family_details.objects.filter(username=username).first()
    user = User.objects.filter(username=username).first()
    data = {
        'details':details,
        'fdetails':fdetails,
        'user':user,
        'uid':username
    }

    return render(request, "staff/upload_details.html",data)

@login_required(login_url='/staff/login')
def add_user(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        rofficer = request.POST.get('rofficer')
        if User.objects.filter(username=username).exists():
            messages.warning(request, "user alredy exist with this username")
        else:
            User.objects.create_user(password=password, username=username, email=email,first_name=fname, last_name=lname)
            obj=profile(related_officer=rofficer,username=username,first_name=fname,last_name=lname)
            obj.save()
            obj2=family_details(username=username,first_name=fname,last_name=lname)
            obj2.save()
       
            messages.success(request, "user added successfully")
        
      
        return redirect('/staff')
    else:
        return HttpResponse("error")

    return HttpResponse('add user')


@login_required(login_url='/staff/login')
def alter_user(request,username):
    username=username
    details = User.objects.filter(username=username).first()
    data = {
        'details':details,
    }

    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        obj2=User.objects.filter(username=username).update(password=password, username=username, email=email,first_name=fname, last_name=lname)
        obj2=profile.objects.filter(username=username).update(username=username,first_name=fname, last_name=lname)
        obj2=family_details.objects.filter(username=username).update( username=username,first_name=fname, last_name=lname)
        
        # User.objects.create_user(password=password, username=username, email=email,first_name=fname, last_name=lname)
        
        return redirect('/staff')
    else:
        
        return render(request, "staff/alter-user.html",data)
    

@login_required(login_url='/staff/login')
def delete_user(request,username):
    username=username
    rm = User.objects.get(username=username)
    rm.delete()
    if profile.objects.filter(username=username).exists():
        prm = profile.objects.get(username=username)
        prm.delete()
    else:
        pass

    if family_details.objects.filter(username=username).exists():
        prm = family_details.objects.get(username=username)
        prm.delete()
    else:
        pass

    # rmp = profile.objects.get(u)
    messages.warning(request, "user deleted successfully")
    return redirect('/staff')


@login_required(login_url='/staff/login')
def upload_media(request,username):
    username=username
    u=User.objects.filter(username=username).first()
   
    uid=u.id
  
    UserIn = User.objects.filter(id=uid).first()
    data = {
        "UserIn":UserIn
    }
    if request.method == "POST":
        dp = request.FILES['dp']

        if media.objects.filter(user_id=uid).exists():
            medias=media.objects.get(user_id=uid)
            medias.delete()
            obj=media(user_id=uid,dp=dp)
            obj.save()
            # obj=media.objects.filter(user_id=uid).update(dp=dp)
        else:
            obj=media(user_id=uid,dp=dp)
            obj.save()

    return render(request, "staff/upload-media.html",data)

@login_required(login_url='/staff/login')
def save_details(request):
    if request.method == "POST":
        mobile = request.POST.get('mobile')
        mstatus = request.POST.get('mstatus')
        dob = request.POST.get('dob')
        height = request.POST.get('height')
        color = request.POST.get('color')
        qualification = request.POST.get('qualification')
        work = request.POST.get('work')
        experience = request.POST.get('experience')
        Hobbies = request.POST.get('Hobbies')
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

        

        
    
        if profile.objects.filter(username=username).exists():
            obj=profile.objects.filter(username=uid).update(user=id,mobile=mobile,marrital_status=mstatus,dob=dob,height=height,color=color,Qualification=qualification,work=work,experience=experience,hobbies=Hobbies,income=Income,medical_condition=medical_condition,city=city,about_me=about,gender=gender,registerfor=regofor)
            obj2=family_details.objects.filter(username=uid).update(user=id,father_name=father_name,father_education=father_education,father_occupation=father_occupation,mother_name=mother_name,mother_education=mother_education,mother_occupation=mother_occupation,brother=brother,sister=sister,relatives=relatives,native_place=native_place)
           
        else:
            # user = User.objects.filter(id=uid).first()
            obj=profile(username=uid,mobile=mobile,marrital_status=mstatus,dob=dob,height=height,color=color,Qualification=qualification,work=work,experience=experience,hobbies=Hobbies,income=Income,medical_condition=medical_condition,city=city,about_me=about,gender=gender,registerfor=regofor)
            obj2=family_details(username=uid,user=id,father_name=father_name,father_education=father_education,father_occupation=father_occupation,mother_name=mother_name,mother_education=mother_education,mother_occupation=mother_occupation,brother=brother,sister=sister,relatives=relatives,native_place=native_place)
            obj.save()
            # obj2.save()
    return redirect('/staff')
    
