from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request, "teacherRater/index.html")


@login_required(login_url='login')
def TeacherProfile(request, name):
    return render(request, "teacherRater/teacherProfile.html", {
        "teacherName": name.capitalize()
    })