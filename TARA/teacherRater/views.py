from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from teacherRater.models import teacherProfile, reviews
from teacherRater.forms import ratingForms

from django.db.models import Avg
# Create your views here.

@login_required(login_url='login')
def index(request):
    teachersList = teacherProfile.objects.all()
    teachReview = reviews.objects.all()
    return render(request, "teacherRater/index.html", {
        "teacherList": teachersList
    })

@login_required(login_url='login')
def searchPage(request, searchname):
    searchResult = teacherProfile.objects.filter(name__contains=searchname)
    print(searchResult)
    return render(request, "teacherRater/searchPage.html", {
        "search": searchResult
    })

@login_required(login_url='login')
def TeacherProfile(request, teacher_id):
    # Grab all necessary data (user, teacher, and if user has reviewed)
    currTeacher = teacherProfile.objects.get(pk=teacher_id)
    currUser = request.user
    teacherReviews = reviews.objects.filter(teacher_id=teacher_id)
    userHasReviewed = teacherReviews.filter(user_id=currUser)

    # Check if teacher has a review
    if teacherReviews:
        # Create Average
        ratingData = teacherReviews.aggregate(avgUnderstand=Avg('understandability'), avgComms=Avg('communication'),
                                              avgTeachMethod=Avg('teachingMethod'))
        ratingData['avgUnderstand'] = round(ratingData['avgUnderstand'], 2)
        ratingData['avgComms'] = round(ratingData['avgComms'], 2)
        ratingData['avgTeachMethod'] = round(ratingData['avgTeachMethod'], 2)
        overallReview = round((ratingData['avgUnderstand'] + ratingData['avgComms'] + ratingData['avgTeachMethod']) / 3,
                              2)
    # The dictionary/Reviews are empty
    else:
        ratingData = {'avgUnderstand': 0, 'avgComms': 0, 'avgTeachMethod': 0}
        overallReview = 0

    if request.method == 'POST':
        # If userHasReviewed has a value, then he has reviewed
        if userHasReviewed:
            # This should return a YOU HAVE ALREADY REVIEWED SCREEN
            return HttpResponse("You already reviewed dummy")
        form = ratingForms(request.POST)
        if form.is_valid():
            # Grab information from forms, and save it into the database
            currCommentReview = form.cleaned_data['commentsReview']
            cUnderstand = form.cleaned_data['understandability']
            cComms = form.cleaned_data['communication']
            cTeachMethod = form.cleaned_data['teachingMethod']
            anonym = form.cleaned_data['makeAnonymous']
            reviewComment = reviews(user=currUser, teacher=currTeacher, isAnonymous=anonym, understandability=cUnderstand, communication=cComms, teachingMethod=cTeachMethod,
                                    commentReview=currCommentReview)
            reviewComment.save()
    else:
        form = ratingForms()

    return render(request, "teacherRater/teacherProfile.html", {
        "teacher": currTeacher,
        "form": form,
        "reviews": teacherReviews,
        "ratings": ratingData,
        "overallRating": overallReview
    })