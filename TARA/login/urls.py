from django.urls import path
from . import views

urlpatterns = [
    path("", views.loginpage, name="login"),
    path("register/", views.register, name="register"),
    path("logout", views.logoutuser, name="logout"),
    path('token/', views.token_send, name="token_send"),
    path('verify/<auth_token>', views.verify, name="verify"),
    path('error/', views.error_page, name="error")
]