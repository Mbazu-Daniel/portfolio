from django.db import models
from django.urls import reverse


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='resume/images/')
    url = models.URLField(max_length=1000)

    def __str__(self):
        return self.title


class Experience(models.Model):
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    description = models.CharField(max_length=7000, blank= True, null=True)
    date_start = models.CharField(max_length=50)
    date_end = models.CharField(max_length=50, default='Present')


    def __str__(self):
        return self.job_title

    def format_date(self, obj):
        return obj.date.strftime('%b, %Y')


class Skill(models.Model):
    skill = models.CharField(max_length=200)


    def __str__(self):
        return self.skill