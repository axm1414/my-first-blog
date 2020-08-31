from django import forms

from .models import Post, Comment, Resume


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['mobile', 
        'email', 
        'address', 
        'job', 
        'personalProfile', 
        'jobTitle1', 'start_year1', 'start_month1' ,'end_year1', 'end_month1', 'job_description1',
        'jobTitle2', 'start_year2', 'start_month2' ,'end_year2', 'end_month2', 'job_description2'
        ]

