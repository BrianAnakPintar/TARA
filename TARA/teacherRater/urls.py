from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("teacher/<str:teacher_id>", views.TeacherProfile, name="TeacherProfile"),
    path("search", views.searchPage, name="SearchPage"),
    path("aboutUs", views.aboutUs, name="AboutUsPage")
]
