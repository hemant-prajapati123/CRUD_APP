from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from .models import Student
def home(request):
    if request.method=="POST":
        username=request.POST['uname']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
        else:
            messages.info(request,"Invalid username and password")
        return redirect("/")
    else:
        return render(request,'index.html')
def addstudent(request):
    if request.method=='POST':
        s=Student()
        s.name=request.POST['name']
        s.branch=request.POST['branch']
        s.address=request.POST['address']
        s.save()
        messages.success(request,"added sucessfully")
        return redirect("/")
    else:
        return render(request,'addstudent.html')
def showstudent(request):
    data=Student.objects.all()
    return render(request,'index.html',{'data':data})
def deletestudent(request):
    id=request.GET['id']
    Student.objects.filter(id=id).delete()
    data=Student.objects.all()
    return render(request,'index.html',{'data':data})