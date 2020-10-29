from django.db import models

# Create your models here.

class Team(models.Model):

    name = models.CharField(max_length=50,)

    def __str__(self):

        return self.name

class Member(models.Model):

    ROLE_CHOICES = [('Convener', 'Convener'), ('Co-convener', 'Co-convener'), ('Member', 'Member')]

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    role = models.CharField(max_length=100, blank=False, choices = ROLE_CHOICES)
    profilepic = models.ImageField(upload_to='team-profilepics', blank=True)
    github = models.URLField(max_length=1000, blank=True)
    linkedIn = models.URLField(max_length=1000, blank=True)
