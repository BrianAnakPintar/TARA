from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from teacherRater.models import teacherProfile, reviews
from teacherRater.forms import ratingForms

from django.core.exceptions import PermissionDenied

# Create your views here.

@login_required(login_url='login')
def index(request):
    teachersList = teacherProfile.objects.all()
    return render(request, "teacherRater/index.html", {
        "teacherList": teachersList
    })


@login_required(login_url='login')
def TeacherProfile(request, teacher_id):
    currTeacher = teacherProfile.objects.get(pk=teacher_id)
    currUser = request.user
    teacherReviews = reviews.objects.filter(teacher_id=teacher_id)

    userHasReviewed = teacherReviews.filter(user_id=currUser)

    if request.method == 'POST':
        if userHasReviewed:
            # This should return a YOU HAVE ALREADY REVIEWED SCREEN
            return HttpResponse("You already reviewed dummy")
        form = ratingForms(request.POST)
        if form.is_valid():
            currCommentReview = form.cleaned_data['commentsReview']
            currRating = form.cleaned_data['rate']
            anonym = form.cleaned_data['makeAnonymous']
            reviewComment = reviews(user=currUser, teacher=currTeacher, isAnonymous=anonym, rating=currRating,
                                    commentReview=currCommentReview)
            reviewComment.save()
    else:
        form = ratingForms()

    return render(request, "teacherRater/teacherProfile.html", {
        "teacher": currTeacher,
        "form": form,
        "reviews": teacherReviews
    })