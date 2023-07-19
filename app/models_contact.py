from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=200, null=False)
    address = models.CharField(max_length=200, null=False)
    phone = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.phone