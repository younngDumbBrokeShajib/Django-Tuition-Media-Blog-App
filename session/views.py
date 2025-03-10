from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User #here User is written in uppercase as This is a model name
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
# Create your views here.

def loginUser(request):
    if request.method=="POST":
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                print(username)
                print(password)
                return redirect('homepage')
            else:
                messages.error(request,"Invalid Username or Passowrd")
    else:
        form=AuthenticationForm()
    return render(request,'session/login.html',{'form':form})

def logoutuser(request):
    logout(request)
    messages.success(request,"successfully logout")
    return redirect('homepage')

def changePassword(request):
    if request.method=='POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,user=form.user)
            messages.success(request,'Password Changed')
            return redirect('homepage')
    else:
        form=PasswordChangeForm(user=request.user)
        update_session_auth_hash(request,user=request.user)
    return render(request,'session/change_pass.html',{'form':form})

def userRegis(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            current_site=get_current_site(request)
            mail_subject='An account Created'
            message=render_to_string('session/account.html', {
                'user':user,
                'domain':current_site.domain,
            })
            send_mail=form.cleaned_data.get('email')
            email=EmailMessage(mail_subject,message,to=[send_mail])
            email.send()
            messages.success(request,'user created successfully')
            return redirect('homepage')
    else:
        form=RegistrationForm()
    return render(request,'session/signup.html',{'form':form})

from .forms import UserProfile
from .models import UserModel

def userProfileView(request):
    try:
        instance=UserModel.objects.get(user=request.user)
    except UserModel.DoesNotExist:
        instance=None
    if request.method=="POST":
        if instance:
            form=UserProfile(request.POST,request.FILES,instance=instance)
        else:
            form=UserProfile(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False) #See doc anotated as adding User to the UserModel
            obj.user=request.user
            obj.save()
            messages.success(request,"SUccessfully saved your profile")
            return redirect('homepage')
    else:
        form=UserProfile(instance=instance)
    context={
        'form':form
    }
    return render(request,'session/userproCreate.html',context=context)

def showUserProfileView(request):
    user=request.user
    return render(request,'session/userProfile.html',{'user':user})
