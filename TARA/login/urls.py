from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.loginpage, name="login"),
    path("register/", views.register, name="register"),
    path("logout", views.logoutuser, name="logout"),
    path('token/<str:username>', views.token_send, name="token_send"),
    path('verify/<auth_token>', views.verify, name="verify"),
    path('error/', views.error_page, name="error"),
    path('reset_password', auth_views.PasswordResetView.as_view(template_name="login/password_reset.html"), name="reset_password"),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="login/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="login/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="login/password_reset_done.html"), name="password_reset_complete")
]
