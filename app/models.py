from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#change forms register django
class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_categories', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


# Create your models here.
class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='product')
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    # náº¿u chÆ°a cÃ³ áº£nh thÃ¬ hiá»ƒn thá»‹ áº£nh loi
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url




