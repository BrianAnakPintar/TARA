from django.contrib.auth.models import User
from django.db import models

lessonChoices = [
    ('All', 'All'),
    ('ACC', 'Akuntansi'),
    ('ART', 'Art'),
    ('BI', 'Bahasa Indonesia'),
    ('BS', 'Biblical Studies'),
    ('BIO', 'Biologi'),
    ('CIV', 'Civics'),
    ('ECO', 'Ekonomi'),
    ('ENG', 'English'),
    ('PHYS', 'Fisika'),
    ('GEO', 'Geologi'),
    ('CHEM', 'Kimia'),
    ('COMP', 'Komputer'),
    ('MAN', 'Mandarin'),
    ('MATH', 'Math'),
    ('MUS', 'Music'),
    ('HIS', 'Sejarah'),
    ('SOS', 'Sosiologi'),
    ('IDK', 'Other')
]

Grades = [
    ('All', 'All'),
    (7, 'Grade 7'),
    (8, 'Grade 8'),
    (9, 'Grade 9'),
    (10, 'Grade 10'),
    (11, 'Grade 11'),
    (12, 'Grade 12'),
    (0, 'Other')
]

# Create your models here.
class teacherProfile(models.Model):
    name = models.CharField(max_length=128)
    picture = models.URLField()
    comment = models.TextField(max_length=3000, blank=True)
    grade = models.IntegerField(choices=Grades, default=0)
    education = models.CharField(max_length=255)
    subjects = models.CharField(max_length=4, choices=lessonChoices, default='IDK')
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}|{self.name}|Subject:{self.subjects}"

understandabilityChoices = [
    (1, '1|Very hard to understand'),
    (2, '2|Hard to understand'),
    (3, '3|Understandable'),
    (4, '4|Easy to understand'),
    (5, '5|I understand everything')
]

communicationChoices = [
    (1, '1|Really bad communication'),
    (2, '2|Bad communication'),
    (3, '3|Communicates well'),
    (4, '4|Communicates really well'),
    (5, '5|Communicates clearly and often')
]

teachingMethodChoices = [
    (1, '1|Horrible'),
    (2, '2|Bad'),
    (3, '3}Average'),
    (4, '4|Good'),
    (5, '5|Amazing')
]



class reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher = models.ForeignKey(teacherProfile, on_delete=models.CASCADE)
    isAnonymous = models.BooleanField(default=True)
    understandability = models.PositiveSmallIntegerField(choices=understandabilityChoices, default=1)
    communication = models.PositiveSmallIntegerField(choices=communicationChoices, default=1)
    teachingMethod = models.PositiveSmallIntegerField(choices=teachingMethodChoices, default=1)
    commentReview = models.TextField(max_length=3000, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.teacher}|U:{self.understandability} C:{self.communication} T:{self.teachingMethod}"

