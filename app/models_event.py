from django.db import models


class Events(models.Model):
    name = models.CharField(max_length=200, null=True)
    intro = models.TextField(null=False)
    publication_date = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=500, null=True)
    publication_time = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
