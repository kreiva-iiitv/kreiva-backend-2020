from django.db import models

# Create your models here.

class Team(models.Model):

    name = models.CharField(max_length=50,)

    def __str__(self):

        return self.name

class TeamMember(models.Model):

    # ROLE_CHOICES = [('Lead', 'Lead'), ('Co-Lead', 'Co-Lead'), ('Member', 'Member'), ('Coordinator', 'Coordinator')]

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    role = models.CharField(max_length=100, blank=False)
    profilepic = models.ImageField(upload_to='team-profilepics', blank=True)
    github = models.URLField(max_length=1000, blank=True)
    linkedIn = models.URLField(max_length=1000, blank=True)

    def __str__(self):
        return f'{self.team}: {self.first_name} {self.role}'