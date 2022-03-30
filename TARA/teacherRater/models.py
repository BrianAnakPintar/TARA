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

understandabilityChoices = [
    (1, '1|Hard to understand'),
    (2, '2|Understandable'),
    (3, '3|Easy to understand'),
    (4, '4|Very easy to understand'),
    (5, '5|I can understand everything the teacher say!')
]

communicationChoices = [
    (1, '1|Teacher rarely communicates'),
    (2, '2|Teacher communicates sometimes'),
    (3, '3|'),
    (4, '4|'),
    (5, '5|')
]

teachingMethodChoices = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),

]

# Should prob delete this
RatingChoices = [
    (1, 'Awful'),
    (2, 'Ok'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Amazing!')
]

class reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher = models.ForeignKey(teacherProfile, on_delete=models.CASCADE)
    isAnonymous = models.BooleanField(default=True)
    understandability = models.PositiveSmallIntegerField(choices=understandabilityChoices, default=1)
    communication = models.PositiveSmallIntegerField(choices=communicationChoices, default=1)
    teachingMethod = models.PositiveSmallIntegerField(choices=teachingMethodChoices, default=1)
    commentReview = models.TextField(max_length=3000, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.teacher}|U:{self.understandability} C:{self.communication} T:{self.teachingMethod}"

