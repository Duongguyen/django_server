from django.db import models


#change forms register django
class CategoryBlog(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_categories', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name


# Create your models here.
class Blog(models.Model):
    stt = models.IntegerField(null=False)
    category = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)
    source = models.CharField(max_length=200, null=False)
    description = models.CharField(null=True, blank=True, max_length=200,)
    publication_date = models.DateTimeField()
    poster = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title

    # náº¿u chÆ°a cÃ³ áº£nh thÃ¬ hiá»ƒn thá»‹ áº£nh loi
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class CategoryPhoto(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_categories', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
