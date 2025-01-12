from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User #here User is written in uppercase as This is a model name
from django.contrib import messages
from django.urls import reverse_lazy
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
            update_session_auth_hash(request,user=form.user)
            messages.success(request,'Password Changed')
            return redirect('homepage')
    else:
        form=PasswordChangeForm(user=request.user)
        update_session_auth_hash(request,user=request.user)
    return render(request,'session/change_pass.html',{'form':form})




