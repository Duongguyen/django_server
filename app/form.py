from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models

from app.models import CategoryBlog, Blog, Photo


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['stt', 'category', 'title', 'image', 'source', 'description', 'publication_date', 'poster']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'password1', 'password2']


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['name', 'category', 'description', 'image']