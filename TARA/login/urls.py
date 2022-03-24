from django.urls import path
from . import views

urlpatterns = [
    path("", views.loginpage, name="login"),
    path("register/", views.register, name="register"),
    path("logout", views.logoutuser, name="logout"),
    path("activate-user/<uidb64>/<token>", views.activateaccount, name="activate")
]