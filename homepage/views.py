from django.shortcuts import redirect, render

# Create your views here.
from django.urls import path
from django.http import HttpResponse
from . models import Watches, WatchesUploads, Laptop, Mobile, Graphic, Processor, Accessory
from . forms import UploadForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def Home(request):
    watches=Watches.objects.all()
    context={'watches_t': watches}
    return render(request,"home.html",context)
                        
def About(request):
    return render(request, "about.html")

def custupload(request):
    allwatches=WatchesUploads.objects.all()
    context={'allwatches_t': allwatches}
    return render(request, "custupload.html",context)

def watch(request):
    watches=Watches.objects.all()
    context={'watches_t': watches}
    return render(request, "watch.html",context)

def laptop(request):
    laptop=Laptop.objects.all()
    context={'laptop_t': laptop}
    return render(request, "laptop.html",context)

def mobile(request):
    mobile=Mobile.objects.all()
    context={'mobile_t': mobile}
    return render(request, "mobile.html",context)

def graphic(request):
    graphic=Graphic.objects.all()
    context={'graphic_t': graphic}
    return render(request, "graphic.html",context)

def processor(request):
    processor=Processor.objects.all()
    context={'processor_t': processor}
    return render(request, "processor.html",context)

def accessory(request):
    accessory=Accessory.objects.all()
    context={'accessory_t': accessory}
    return render(request, "accessory.html",context)


@login_required
def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UploadForm()

    return render(request, "watchupload.html",{'form' : form})


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=user_name, password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return render(request, "login.html",{'form' : form}) 
    else:
        form= AuthenticationForm()

    return render(request, "login.html",{'form' : form})  


def signup_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save() 
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {'form': form})


def logout_user(request):
    logout(request)
    return redirect('home')