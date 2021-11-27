from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import *
from API.models import *
import requests

# Create your views here.
def Register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO, "Registration Success.")
                return redirect('start')
            else:
                messages.add_message(request,messages.INFO, f"{ form.errors }")
        content = {'form' : form }
        return render(request,"LoginPage.html",content) 

def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return HttpResponse("error login")
        content = {'form' : form }
        return render(request,"LoginPage.html",content)

def Logout(request):
    logout(request)
    return redirect('start')

@login_required(login_url='start')
def Home(request):
    respond = requests.get("http://127.0.0.1:8000/api/UserKind/")
    userKind = respond.json()
    current_user = request.user
    current_user_id = current_user.id
    for user in userKind:
        if current_user_id == user['user']:
            current_user_type = user
    if current_user_type['is_developer']:
        response = requests.get("http://127.0.0.1:8000/api/BugReport/")
        bugData = response.json()
        content = {}
        content.update({"bugs" : bugData})
        return render(request,"DeveloperHomePage.html", content)
    else:
        if request.method == 'POST':
            userName = request.POST.get('user_name')
            userPhoneNumber = request.POST.get('user_phoneNumber')
            userEmail = request.POST.get('user_email')
            bugName = request.POST.get('bug_name')
            bugDescription = request.POST.get('feedback_form')

            bugDetails = BugDetails(bugName=bugName, userName=userName, userEmail=userEmail, userPhoneNumber=userPhoneNumber, description=bugDescription)
            bugDetails.save()

            messages.add_message(request, messages.INFO, "Your bug has been successfully recorded.")
        return render(request,"CustomerHomePage.html")

@login_required(login_url='start')
def SingleBugReport(request, bug_id):
    response = requests.get("http://127.0.0.1:8000/api/BugReport/")   
    engineer_response = requests.get("http://127.0.0.1:8000/api/engineers/")
    engieerData = engineer_response.json() 
    bugData = response.json()
    for bug in bugData:
        if bug['id'] == bug_id:
            bugDetails = bug
    content = {}
    content.update({'bugDetail' : bugDetails})
    content.update({'engineers' : engieerData})
    return render(request, "BugPage.html", content)

@login_required(login_url='start')
def UpdateBugReport(request,bug_id,engineer_id,status):
    engineer_response = requests.get("http://127.0.0.1:8000/api/engineers/")
    engieerData = engineer_response.json()
    for engineer in engieerData:
        if engineer['id'] == engineer_id:
            selectedEngineer = engineer
    selectedEngineerName = selectedEngineer['name']
    selectedEngineerDesignation = selectedEngineer['designation']
    bugDetail = BugDetails.objects.filter(id=bug_id).update(engineerName=selectedEngineerName, engineerDesignation=selectedEngineerDesignation, progressStatus=status)
    return HttpResponseRedirect(reverse('bug_page', args=[bug_id] ))