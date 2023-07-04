from tkinter import messagebox

from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# from tkinter import *
# from tkinter import messagebox
#
# root = Tk()


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['c_password']
        # agree = request.POST['checked']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email is already linked with another account")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save();
                return redirect('login')
                # messages.info(request, "User created successfully")
        # elif agree != 'yes':
        #     messages.info(request, "Please agree the terms and conditions to create user.")
        else:
            messages.info(request, "Password does not match")
    return render(request, "register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')

# root.mainloop()
