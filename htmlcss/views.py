from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
def home(request):
    return render(request,'index.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email= request.POST['email']
        psw = request.POST['psw']
        psw1=request.POST['psw1']
        l=[]
        m="@gmail.com"
        for i in email:
            l.append(i)
        d = l[(len(l) - 10):]
        s = ""
        for i in d:
            s = s + i
        if psw==psw1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"already user exists with same name")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            elif m!=s:
                messages.info(request,"mail is wrong")
                return redirect('register')

            else:
                user=User.objects.create_user(email=email,password=psw,username=username)
                user.save();
                messages.info(request,"user created")
                return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'index.html')

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')

    else:
        return render(request,'index.html')

