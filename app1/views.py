from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from app1.models import profile, family_details, media
from django.contrib import messages

import random
import string


def home(request):
    from app1.models import profile, family_details, media
    featured1 = profile.objects.filter(is_featured=1)[:8]
    # featured2 = profile.objects.filter(is_featured=1)[8:]

    if request.user.is_authenticated:

        if request.user.profile.is_mail_verified == False:
            return redirect('/fvmail')
        else:

            data = {
                'featured1': featured1,
                # 'featured2':featured2,
            }

            return render(request, "theme/index.html", data)

    data = {
        'featured1': featured1,
        #   'featured2':featured2,
    }

    return render(request, "theme/index.html", data)


def login(request):
    from app1.models import profile, family_details, media

    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        user = auth.authenticate(username=uname, password=pwd)

        if profile.objects.filter(username=uname).exists():

            if user is not None:
                auth.login(request, user)

                messages.success(request, "Successfully Loged In .. ")

                return redirect('/')
            else:
                messages.error(request, "Invalid Credentials Please Try Again.. ")

        else:

            messages.error(request,
                           "Profile Data Not Found Please Contact With Officer (if you are not registered click on join now).. ")

            return redirect('/')

    return render(request, "login.html")


def login1st(request):
    from app1.models import profile, family_details, media

    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        user = auth.authenticate(username=uname, password=pwd)

        if profile.objects.filter(username=uname).exists():

            if user is not None:
                auth.login(request, user)

                messages.success(request, "Successfully Loged In .. ")

                return redirect('/')
            else:
                return HttpResponse("uname , password invalid ")
        else:

            messages.error(request, "Profile Data Not Found Please Contact With Officer .. ")

            return redirect('/')

    return render(request, "login.html")


def logout(request):
    auth.logout(request)

    messages.info(request, "User  Loged Out .. ")

    return redirect('/')


def register(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        regfor = request.POST.get('for')
        gender = request.POST.get('gender')
        lfor = request.POST.get('lfor')
        dob = request.POST.get('dob')
        contact = request.POST.get('contact')

        if User.objects.filter(username=uname).exists():
            messages.error(request, "Profile already exist with this username try another .. ")
            return redirect('/')



        else:
            # u = User(password=pwd, username=uname, email=email,first_name=fname, last_name=lname)    
            User.objects.create_user(password=pwd, username=uname, email=email, first_name=fname, last_name=lname)
            user = auth.authenticate(username=uname, password=pwd)
            auth.login(request, user)
            from app1.models import profile
            obj = profile(user=request.user, is_mail_verified=False, registerfor=regfor, gender=gender, lookingfor=lfor,
                          dob=dob, mobile=contact)
            obj.save()
            return redirect('/profile_home')
    else:
        HttpResponse("faield")


@login_required(login_url='/login')
def profile_home(request):
    if request.user.is_authenticated:

        if request.user.profile.is_mail_verified == False:
            return redirect('/fvmail')
        else:
            return render(request, "theme/profile-home.html")
    return render(request, "theme/profile-home.html")


@login_required(login_url='/login')
def save_personal_detail(request):
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

        from app1.models import profile
        obj = profile.objects.filter(user=request.user).update(mobile=mobile, marrital_status=mstatus, dob=dob,
                                                               height=height, color=color, Qualification=qualification,
                                                               work=work, experience=experience, hobbies=Hobbies,
                                                               income=Income, medical_condition=medical_condition,
                                                               city=city, about_me=about, gender=gender)

    return redirect('/family_details')


@login_required(login_url='/login')
def family_details(request):
    if request.method == "POST":
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

        from app1.models import family_details
        obj = family_details(user=User.objects.get(pk=request.user.id), father_name=father_name,
                             father_education=father_education, father_occupation=father_occupation,
                             mother_name=mother_name, mother_education=mother_education,
                             mother_occupation=mother_occupation, brother=brother, sister=sister, relatives=relatives,
                             native_place=native_place)
        obj.save()

        return redirect('/cdp')

    return render(request, "family_details.html")


def cdp(request):
    if request.method == "POST":
        picture__input = request.FILES['picture__input']
        from app1.models import media
        obj = media(user=User.objects.get(pk=request.user.id), dp=picture__input)
        obj.save()

        return redirect('/')

    return render(request, "cdp.html")


@login_required(login_url='/login')
def all_profiles(request):
    from app1.models import profile, family_details, media

    from match.matchfun import matchfun

    p = profile.objects.all().values('id', 'work', 'Qualification', 'color', 'marrital_status', 'height', 'experience',
                                     'hobbies', 'income', 'medical_condition', 'city')
    profiles = list(p)

    cuser = profile.objects.filter(user=request.user.id).values('id', 'work', 'Qualification', 'color',
                                                                'marrital_status', 'height', 'experience', 'hobbies',
                                                                'income', 'medical_condition', 'city')

    cuserlist = list(cuser)

    gender = request.user.profile.gender
    opogen = ""
    if gender == "Male":
        opogen = "Female"
    elif gender == "Female":
        opogen = "Male"

    mlist = matchfun(profiles, cuserlist)

    print(mlist)

    all_profiles = profile.objects.filter(id__in=mlist, gender=opogen)

    all_profiles = sorted(all_profiles, key=lambda x: mlist.index(x.id))

    for id in all_profiles:
        print(id.id)

    data = {

        'all_profiles': all_profiles
    }
    return render(request, "theme/all_profiles.html", data)


def show_profile(request, id):
    from app1.models import profile, family_details, media,gallery

    profile = profile.objects.filter(user=id)[0]
    gallery = gallery.objects.filter(user=id)

    data = {
        'profile': profile,
        'gallery':gallery,

    }
    return render(request, "theme/profile.html", data)


def gencode():
    N = 5
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    strres = str(res)
    return strres


def sendmail(rec, code):
    from email.message import EmailMessage
    import ssl
    import smtplib

    sender = 'loharprathmesh2023@gmail.com'
    rec = rec
    pwd = 'qeie ijdd gunf aauy'

    code = code

    subject = "Verification For Sathi"

    body = "Verification Code : " + code

    em = EmailMessage()
    em['From'] = sender
    em['To'] = rec
    em['subject'] = subject
    em.set_content(body)

    contex = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contex) as smtp:
        smtp.login(sender, pwd)
        smtp.sendmail(sender, rec, em.as_string())


@login_required(login_url='/login')
def vmail(request):
    code = gencode()

    if request.method == 'POST':
        code = request.POST.get('code')
        ccode = request.POST.get('ccode')

        if code == ccode:
            from app1.models import profile
            profile.objects.filter(user=request.user.id).update(is_mail_verified=True)

            return redirect('/')
        else:
            return render(request, "vmail.html", {'code': code})

    sendmail(request.user.email, code)

    return render(request, "vmail.html", {'code': code})


@login_required(login_url='/login')
def fvmail(request):
    code = gencode()

    if request.method == 'POST':
        code = request.POST.get('code')
        ccode = request.POST.get('ccode')

        if code == ccode:
            from app1.models import profile
            profile.objects.filter(user=request.user.id).update(is_mail_verified=True)

            messages.success(request, "Mail Verified Successfully .. ")

            return redirect('/profile_home')
        else:
            messages.error(request, "Mail Not Verified Please Try Again .. ")
            return render(request, "fvmail.html", {'code': code})

    sendmail(request.user.email, code)

    return render(request, "fvmail.html", {'code': code})


@login_required(login_url='/login')
def change_profile(request):
    return render(request, "theme/edit-profile.html")

# not views
