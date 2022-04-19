from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.auth import authenticate, login, logout
from django.utils.html import strip_tags
from django.template.loader import render_to_string
import threading


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


def send_mail_after_registration(email, token):
    recipient_list = email

    html_content = render_to_string("login/Activateaccount.html", {"token": token})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        "Activate TARA Account",
        text_content,
        settings.EMAIL_HOST_USER,
        [recipient_list]
    )
    email.attach_alternative(html_content, "text/html")
    EmailThread(email).start()

# login page
def loginpage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('login')

        profile_obj = Profile.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('login')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('login')

        login(request, user)
        return redirect('index')

    return render(request, 'login/login.html')


def register(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')

    try:
        if User.objects.filter(username = username).first():
            messages.success(request, "Username is taken")
            return redirect(request, 'login/register.html')
        if User.objects.filter(email = email).first():
            messages.success(request, "Email is taken")
            return redirect(request, 'login/register.html')
        if len(password) < 8:
            messages.success(request, "Password should contain at least 8 characters")
            return redirect(request, 'login/register.html')

        user_obj = User(username=username, email=email)
        user_obj.set_password(password)
        user_obj.save()

        auth_token = str(uuid.uuid4())
        profile_obj = Profile.objects.create(user=user_obj, auth_token=auth_token)
        profile_obj.save()
        send_mail_after_registration(email, auth_token)
        return redirect('token_send')

    except Exception as e:
        print(e)

    return render(request, 'login/register.html')



def token_send(request):
    return render(request, 'login/token_send.html')


def verify(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token=auth_token).first()

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('login')
        else:
            return redirect('error')
    except Exception as e:
        print(e)

        return redirect('login')


#logout from account
def logoutuser(request):
    logout(request)
    return redirect("login")

def error_page(request):
    return render(request, 'login/error.html')


