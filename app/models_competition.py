from django.db import models


class Competition(models.Model):
    name = models.CharField(null=False, max_length=100)
    image = models.ImageField(null=True, blank=True)
    statute = models.CharField(null=False, max_length=100)
    intro = models.TextField(null=False, max_length=100)
    law = models.CharField(null=False, max_length=100)

    def __str__(self):
        return self.name

    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url