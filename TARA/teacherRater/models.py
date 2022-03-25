from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class teacherProfile(models.Model):
    name = models.CharField(max_length=128)
    picture = models.URLField()
    comment = models.TextField(max_length=3000)
    education = models.CharField(max_length=255)
    subjects = models.CharField(max_length=255)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}|{self.name}|Active:{self.isActive}"

RatingChoices = [
    (1, '1 - Awful'),
    (2, '2 - Ok'),
    (3, '3 - Good'),
    (4, '4 - Very Good'),
    (5, '5 - Amazing!')
]


class reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher = models.ForeignKey(teacherProfile, on_delete=models.CASCADE)
    isAnonymous = models.BooleanField(default=True)
    rating = models.PositiveSmallIntegerField(choices=RatingChoices)
    commentReview = models.TextField(max_length=3000, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.teacher}|Rating:{self.rating}"

