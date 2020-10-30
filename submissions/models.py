from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from participant.models import *
from events.models import *

# Create your models here.

class TeamSubmission(models.Model):

    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=100)
    youtube_link = models.URLField()

class IndividialVideoSubmission(models.Model):

    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    youtube_link = models.URLField()

class IndividialPhotoSubmission(models.Model):

    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='submissions', null = True)
    photo_comp = models.ImageField(upload_to='submissions', null = True)
