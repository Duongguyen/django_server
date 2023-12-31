from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models

from app.models import CategoryBlog, Blog, Photo, Customer


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['stt', 'category', 'title', 'image', 'source', 'description', 'publication_date', 'poster']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['name', 'category', 'description', 'image']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone']
