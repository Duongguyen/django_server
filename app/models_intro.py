from django.db import models


class Greeting(models.Model):
    title = models.CharField(null=False, max_length=100)
    description = models.TextField(null=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class IntroFederation(models.Model):
    title = models.CharField(null=False, max_length=100)
    description = models.TextField(null=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url