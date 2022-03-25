from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/<str:teacher_id>", views.TeacherProfile, name="TeacherProfile")
]
