from django.db import models


# Create your models here.
class Athlete(models.Model):
    fullname = models.CharField(null=False, max_length=200)
    object = models.CharField(max_length=200, null=True)
    sex = models.CharField(max_length=5)
    social_network = models.CharField(max_length=200, null=True)
    date_of_birth = models.DateField()
    home_live = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)
    career = models.CharField(max_length=200, null=True)
    archie = models.TextField(null=False, max_length=100)

    def __str__(self):
        return self.fullname

    # náº¿u chÆ°a cÃ³ áº£nh thÃ¬ hiá»ƒn thá»‹ áº£nh loi
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Coach(models.Model):
    fullname = models.CharField(null=False, max_length=200)
    object = models.CharField(max_length=200, null=True)
    sex = models.CharField(max_length=5)
    social_network = models.CharField(max_length=200, null=True)
    date_of_birth = models.DateField()
    home_live = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)
    career = models.CharField(max_length=200, null=True)
    archie = models.TextField(null=False, max_length=100)

    def __str__(self):
        return self.fullname

    # náº¿u chÆ°a cÃ³ áº£nh thÃ¬ hiá»ƒn thá»‹ áº£nh loi
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Referee(models.Model):
    fullname = models.CharField(null=False, max_length=200)
    object = models.CharField(max_length=200, null=True)
    sex = models.CharField(max_length=5)
    social_network = models.CharField(max_length=200, null=True)
    date_of_birth = models.DateField()
    home_live = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)
    career = models.CharField(max_length=200, null=True)
    archie = models.TextField(null=False, max_length=100)

    def __str__(self):
        return self.fullname

    # náº¿u chÆ°a cÃ³ áº£nh thÃ¬ hiá»ƒn thá»‹ áº£nh loi
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
