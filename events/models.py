from django.db import models

# Create your models here.

class Event(models.Model):

    name = models.CharField(max_length=50)
    poster = models.ImageField(upload_to='events-poster', blank=True)
    short_description = models.CharField(max_length=200, blank=True)
    long_description = models.TextField(blank=True)
    prize = models.IntegerField(blank=True)
    venue = models.CharField(max_length=255, blank=True)
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)
    rules_doc = models.FileField(upload_to='rules', blank=True)
    instagram = models.URLField(max_length = 200, blank=True)
    facebook = models.URLField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    google_form_link = models.URLField(max_length=200, blank=True)

    def __str__(self):

        return self.name

class Member(models.Model):

    ROLE_CHOICES = [('Convener', 'Convener'), ('Co-convener', 'Co-convener'), ('Committee-Coordinator', 'Committee-Coordinator')]

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=100, choices = ROLE_CHOICES)
    phone = models.CharField(blank=True, max_length=20)

    def __str__(self):

        return f"{self.event}: {self.first_name} {self.role}"
