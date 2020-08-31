from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime
from django.forms import Form, ChoiceField


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
    

class Resume(models.Model):
        author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        title = "Andrei Mihai - Resume"
        mobile = models.CharField(max_length=100)
        email = models.EmailField(max_length=100)
        address = models.CharField(max_length=100)
        job = models.CharField(max_length=100)
        personalProfile = models.TextField()
        jobTitle1 = models.CharField(max_length=100)
        jobTitle2 = models.CharField(max_length=100)
        YEAR_CHOICES = [(y,y) for y in range(2010, datetime.date.today().year+1)]
        MONTH_CHOICES = [(m,m) for m in range(1,13)]
        YEAR_CHOICES.insert(0, ('',''))
        MONTH_CHOICES.insert(0, ('',''))
        start_year1 = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
        start_month1 = models.IntegerField(choices=MONTH_CHOICES, default=datetime.datetime.now().month)
        end_year1 = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
        end_month1 = models.IntegerField(choices=MONTH_CHOICES, default=datetime.datetime.now().month)
        start_year2 = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
        start_month2 = models.IntegerField(choices=MONTH_CHOICES, default=datetime.datetime.now().month)
        end_year2 = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
        end_month2 = models.IntegerField(choices=MONTH_CHOICES, default=datetime.datetime.now().month)
        job_description1 = models.TextField()
        job_description2 = models.TextField()
        created_date = models.DateTimeField(default=timezone.now)
        published_date = models.DateTimeField(blank=True, null=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    