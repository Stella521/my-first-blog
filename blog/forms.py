#from django.db import models

# Create your models here.

from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text', )



