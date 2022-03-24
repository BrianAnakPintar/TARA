from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_str, force_bytes
from .utils import generatetoken
from .models import UserTARA
from django.core.mail import EmailMessage
from django.conf import settings


def sendverificationemail(user, request):
    currentsite = get_current_site(request)
    emailsubject= "Activate your account"
    emailbody = render_to_string("login/activate.html", {"user": user,
                                                         "domain": currentsite,
                                                         "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                                                         "token": generatetoken.make_token(user)})

    email = EmailMessage(subject=emailsubject, body=emailbody, from_email=settings.EMAIL_FROM_USER, to=[user.email])
    email.send()


# login page
def loginpage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if not user.verifiedemail:
            messages.error(request, "Your email is not verified. Please verify your email")
            return render(request, "login/login.html")

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
                username = request.POST.get("username")
                email = request.POST.get("email")
                user = UserTARA.objects.create_user(username=username, email=email)
                sendverificationemail(user, request)
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


def activateaccount(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserTARA.objects.get(pk=uid)
    except Exception as e:
        user = None
    if user and generatetoken.check_token(user, token):
        user.verifiedemail = True
        user.save()

        messages.success(request, "Email verified")
        return redirect('login')

    return render(request, 'login/activate-failed.html', {"user": user})
