from django.db import models


class Group(models.Model):
    name_group = models.CharField(null=False, max_length=100)
    subject = models.CharField(null=False, max_length=100)
    image = models.ImageField(null=True, blank=True)
    year = models.CharField(null=False, max_length=100)
    social_network = models.CharField(null=False, max_length=100)
    intro = models.TextField(null=False, max_length=100)
    achier = models.CharField(null=False, max_length=100)

    def __str__(self):
        return self.name_group

    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url