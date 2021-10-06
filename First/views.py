from django.contrib.auth import get_user_model, login as auth_login , logout as auth_logout
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from .models import *
import random
from django.contrib.auth.models import User,auth
# from .twilio_fun import *
# Create your views here.

ACCOUNT_SID = 'AC4e6b71910edc727de5a4b32e82ddd527'
AUTH_TOKEN = 'cc5d59a41783f8306f4e6125fb43f946'

# def update(request):
#     get_singer=request.POST.get('singer')
#     list = []
#     f=request.POST.getlist('singer')

#     print(f)
#     return render(request,'update.html')

@login_required(login_url='/')
def user_details(request):
    user= request.user.id
    get_todo =Register.objects.filter(user = request.user)
    return render(request,'user_details.html',{'user':user,'item':get_todo})

@login_required(login_url='/')
def main(request):
    items= Register.objects.filter(user=request.user.id)
    return render(request,'main.html',{'item':items})

@login_required(login_url='/')
def edit(request,id):
    print(request.user)
    if request.method == "POST":
        get_user= request.POST.get('username')
        get_number= request.POST.get('number')
        get_gender= request.POST.get('gender')
        get_singer=request.POST.getlist('singer')
        
        get_id = Register.objects.get(id=id)
        get_id.Username= get_user
        get_id.Number= get_number
        get_id.Gender= get_gender
        get_id.Singer=get_singer
        get_id.save()

        get_user_id=User.objects.get(username=request.user)
        get_user_id.username= get_user
            # get_user_id.set_password(get_number)
        get_user_id.save()

        print(get_gender,get_id,get_number,get_user)
        return redirect('/user_details')
        # items= Register.objects.filter(user=request.user.id)
        # return render(request,'main.html',{'item':items})
    items= Register.objects.filter(user=request.user.id)
    return render(request,'edit.html',{'item':items})


# def index(request):
#     return render(request,'index.html')

def login(request):
    if request.method == "POST":
        get_user=request.POST.get('username')
        get_number = request.POST.get('passcode')
        print(get_user,get_number)
        user_auth = authenticate(username=get_user,password=get_number)

        print(user_auth)
        if user_auth:
            auth.login(request,user_auth)
            print(user_auth)
            messages.success(request, 'Auth User')
            return redirect('/main')
        else:
            messages.warning(request, 'Unable to access, register now')
            return redirect('/')

    return render(request,'login.html')

def register(request):
    if request.method == "POST":
        get_user=request.POST.get('username')
        get_password=request.POST.get('passcode')
        get_number = request.POST.get('number')
        # myfile = request.FILES['myfile']    
        otp_code = random.randint(10000, 99999)
        # request.session['userName']=get_user
        # request.session['userNumber']=get_number

        print("Username",get_user,"Number",get_number,"Password:",get_password)
        user_obj = Register.objects.filter(Number=get_number).exists()
        if user_obj:
            messages.warning(request, 'Already taken this number,try with diffrent')
            print("")
            return redirect('/register')
        else:
            user_model = User.objects.create_user(username=get_user,password=get_password)
            user_model.set_password(get_password)
            user_obj = Register(Username=get_user,Passcode=get_password,Number=get_number,user = user_model)
            if len(request.FILES)!=0:
                user_obj.Image=request.FILES['image']
            # msg = f"OTP: {str(otp_code)}"
            # send_sms(ACCOUNT_SID,AUTH_TOKEN,msg,"+19363427869","+917837040632")
            save_otp=OTP.objects.create(user_otp=otp_code)
            save_otp.save()
            user_model.save()
            print(otp_code)
            auth.login(request,user_model)
            user_obj.save()
            auth.login(request,user_model)               
            return redirect('/token')
    return render(request,'register.html')

def token(request):

    if request.method == "POST":
        # UserName=request.session['userName']
        otp_1 = request.POST.get('otp')
        # print(otp_1)
        otp_obj = OTP.objects.filter(user_otp=otp_1).exists()
        if otp_obj:
            user_add=OTP.objects.create(user=request.user)
            print("Match")
            user_add.save()
            return redirect('main')
        else:
            print("Your  OTP Code  didn't match!")
            return redirect('token')

    else:        
        return render(request,'token.html')

def logout(request):
    auth.logout(request)
    return redirect('/')