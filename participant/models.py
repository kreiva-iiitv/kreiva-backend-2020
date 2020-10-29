from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField



class Participant(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.CharField(max_length = 100)
    phone_number = PhoneNumberField()

    def __str__(self):

        return self.user.username


# Create your models here.
