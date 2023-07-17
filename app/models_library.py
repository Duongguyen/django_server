from django.db import models


class LibraryText(models.Model):
    name = models.CharField(null=False, max_length=100)
    create_at = models.DateField()
    tag = models.CharField(null=True, max_length=1000)
    uploaded_file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def FileURL(self):
        try:
            url = self.uploaded_file.url
        except:
            url = ''
        return url


class LibraryLaw(models.Model):
    name = models.CharField(null=False, max_length=100)
    create_at = models.DateField()
    tag = models.CharField(null=True, max_length=1000)
    uploaded_file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def FileURL(self):
        try:
            url = self.uploaded_file.url
        except:
            url = ''
        return url


class LibraryReferences(models.Model):
    name = models.CharField(null=False, max_length=100)
    create_at = models.DateField()
    tag = models.CharField(null=True, max_length=1000)
    uploaded_file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def FileURL(self):
        try:
            url = self.uploaded_file.url
        except:
            url = ''
        return url
