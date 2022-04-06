from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from teacherRater.models import teacherProfile, reviews
from teacherRater.forms import ratingForms

from django.db.models import Avg
from django.db.models import Count
# Create your views here.

def getOverallReviews(teacherReviews):
    # Check if teacher has a review
    if teacherReviews:
        # Create Average
        ratingData = teacherReviews.aggregate(avgUnderstand=Avg('understandability'), avgComms=Avg('communication'),
                                              avgTeachMethod=Avg('teachingMethod'))
        ratingData['avgUnderstand'] = round(ratingData['avgUnderstand'], 2)
        ratingData['avgComms'] = round(ratingData['avgComms'], 2)
        ratingData['avgTeachMethod'] = round(ratingData['avgTeachMethod'], 2)
        return round((ratingData['avgUnderstand'] + ratingData['avgComms'] + ratingData['avgTeachMethod']) / 3, 2)
    # The dictionary/Reviews are empty
    else:
        return 0

def getReviewCount(teacherReviews):
    if teacherReviews:
        totalReview = teacherReviews.aggregate(count=Count('understandability'))
        return totalReview['count']
    else:
        return 0

class Teacher:
    def __init__(self, teacherID, name, overallRating, totalReviews, picture, lesson):
        self.teacherID = teacherID
        self.name = name
        self.overallRating = overallRating
        self.totalReviews = totalReviews
        self.picture = picture
        self.lesson = lesson

@login_required(login_url='login')
def index(request):
    currId = 0
    teachersList = teacherProfile.objects.all()
    teachersAndInfo = []
    for teacher in teachersList:
        currId += 1
        teacherReviews = reviews.objects.filter(teacher_id=currId)
        teachersAndInfo.append(Teacher(teacher.pk, teacher.name, getOverallReviews(teacherReviews), getReviewCount(teacherReviews), teacher.picture, teacher.subjects))

    return render(request, "teacherRater/index.html", {
        "teacherList": teachersList,
        "teacherRatings": teachersAndInfo
    })

@login_required(login_url='login')
def searchPage(request):
    if request.method == 'GET':
        searchInput = request.GET.get('searchInput')

    search = []
    searchResult = teacherProfile.objects.filter(name__contains=searchInput)
    for teacher in searchResult:
        currId = teacher.pk
        teacherReviews = reviews.objects.filter(teacher_id=currId)
        search.append(Teacher(teacher.pk, teacher.name, getOverallReviews(teacherReviews), getReviewCount(teacherReviews) ,teacher.picture, teacher.subjects))

    return render(request, "teacherRater/searchPage.html", {
        "search": search,
        "searchText": searchInput
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
        # Find how many reviews
        reviewCount = getReviewCount(teacherReviews)

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
        reviewCount = 0

    if request.method == 'POST':
        # If userHasReviewed has a value, then he has reviewed
        if userHasReviewed:
            # This should return a YOU HAVE ALREADY REVIEWED SCREEN
            return render(request, "teacherRater/reviewerror.html")
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
            # Return redirects automatically "Refreshes the page"
            # return redirect(TeacherProfile, teacher_id)
            return render(request, "teacherRater/reviewSuccess.html")
    else:
        form = ratingForms()

    return render(request, "teacherRater/teacherProfile.html", {
        "teacher": currTeacher,
        "form": form,
        "reviews": teacherReviews,
        "ratings": ratingData,
        "overallRating": overallReview,
        "myreview": userHasReviewed,
        "reviewCount": reviewCount
    })

def aboutUs(request):
    return render(request, "teacherRater/aboutus.html")

def review_delete(request, teacherId):
    # Get the review that you want to delete
    review = reviews.objects.filter(teacher_id=teacherId, user_id=request.user.pk)
    if request.method == 'POST':
        # Delete the review
        review.delete()
        # Go back to previous page
        return render(request, "teacherRater/deleteSuccess.html", {'teachID': teacherId})
    return redirect(TeacherProfile, teacherId)