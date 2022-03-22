from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "teacherRater/index.html")

def TeacherProfile(request, name):
    return render(request, "teacherRater/teacherProfile.html", {
        "teacherName": name.capitalize()
    })