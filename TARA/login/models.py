from django.db import models
from django.contrib.auth.models import AbstractUser

class UserTARA(AbstractUser):
    verifiedemail = models.BooleanField(default=False)

    def __str__(self):
        return self.email

