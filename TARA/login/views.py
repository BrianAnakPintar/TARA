from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt  # csrf error
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# login page
@csrf_exempt
def loginpage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("teacherRater/index")
    return render(request, 'login/login.html')


# register page
@csrf_exempt
def register(request):
    form = CreateUserForm()

    # if input is valid, save form (Usernames unused, hash pass, etc)
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "Account successfully created")

            return redirect("login")

    return render(request, 'login/register.html', {"form": form})
