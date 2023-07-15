from django.db import models


class Partner(models.Model):
    name = models.CharField(null=False, max_length=100)
    address = models.CharField(null=False, max_length=100)
    image = models.ImageField(null=True, blank=True)
    phone = models.CharField(null=False, max_length=100)
    social_network = models.CharField(null=False, max_length=100)
    email = models.TextField(null=False, max_length=100)

    def __str__(self):
        return self.name

    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url