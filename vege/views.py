from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q,Sum
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
def home(request):
    return render(request,'base.html')
@login_required(login_url="/login_page")
def reciepe(request):
    if request.method=="POST":
        data=request.POST
        reciepe_name=data.get("reciepe_name")
        reciepe_description=data.get("reciepe_description")
        reciepe_image=request.FILES.get("reciepe_image")
        
        reciepes.objects.create(
            reciepe_name=reciepe_name,
            reciepe_description=reciepe_description,
            reciepe_image=reciepe_image
        )

        return redirect("/reciepes/")

    queryset=reciepes.objects.all()

    if request.GET.get("search"):
        search=request.GET.get("search")
        queryset=queryset.filter(
            Q(reciepe_name__icontains=search)|
            Q(reciepe_description__icontains=search)
            )
    context={'queryset':queryset}


    return render(request,"reciepes.html",context)


def delete_reciepe(request, id):
    queryset=reciepes.objects.get(id=id)
    queryset.delete()
    


    return redirect("/reciepes/")
def update_reciepe(request,id):
    queryset=reciepes.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        reciepe_name=data.get("reciepe_name")
        reciepe_description=data.get("reciepe_description")
        reciepe_image=request.FILES.get("reciepe.image")

        queryset.reciepe_name=reciepe_name
        queryset.reciepe_description=reciepe_description
        if reciepe_image:
            queryset.reciepe_image=reciepe_image
        queryset.save()
        return redirect("/reciepes")


    context={"update":queryset}

    return render(request,"update_reciepe.html",context)
def login_page(request):
    if request.method=="POST":
        data=request.POST
        username=data.get("username")
        password=data.get("password")

        if not User.objects.filter(username=username).exists():
            messages.error(request,"Invalid Username")
            return redirect("/login_page")

        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,"Invalid Password")
            return redirect("/login_page/")
        else:
            login(request,user)
            return redirect("/reciepes")
    


    return render(request,"login_page.html")
def register(request):
    if request.method=="POST":
        data=request.POST
        first_name=data.get("first_name")
        last_name=data.get("last_name")
        username=data.get("username")
        password=data.get("password")

        user=User.objects.filter(username=username)
        if user.exists():
            messages.error(request,"username already taken")
            return redirect("/register_page/")

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            
        )
        user.set_password(password)
        user.save()
        messages.info(request,"Account Created Successfully")
        return redirect("/register_page/")

    return render(request,"register.html")
def logout_page(request):
    logout(request)
    return redirect("/login_page/")

def student_page(request):
    queryset=Student.objects.all()
    if request.GET.get("search"):
        search=request.GET.get("search")
        queryset=queryset.filter(
            Q(student_name__icontains=search)|
            Q(student_email__icontains=search)|
            Q(student_id__student_id__icontains=search)|
            Q(department__department__icontains=search)

        )
    context={"student":queryset}
    return render(request,"student_page.html",context)
def details(request,student_id):
    queryset=SubjectMarks.objects.filter(student__student_id__student_id=student_id)
    name=Student.objects.filter(student_id__student_id__icontains=student_id)
    for n in name:
        res=n.student_name
    
    total=queryset.aggregate(total=Sum('marks'))
    print(total)
    context={"details":queryset,'res':res,'total':total}
    return render(request,"details.html",context)