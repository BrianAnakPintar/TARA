from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

# login page
def loginpage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.info(request, "Username or Password is incorrect")

    return render(request, 'login/login.html')


# register page
def register(request):
    form = CreateUserForm()
    isEmailtaken = False
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            try:
                form.save() #make account
                messages.success(request, "Account successfully made")
                return redirect("login")

            except IntegrityError:
                isEmailtaken = True
                return render(request, 'login/register.html', {"form": form, "emailerror":isEmailtaken}) # email error

    return render(request, 'login/register.html', {"form": form, "emailerror": isEmailtaken})  # run main function


#logout from account
def logoutuser(request):
    logout(request)
    return redirect("login")
