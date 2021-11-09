from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe
from django.conf import settings
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = RichTextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    old_price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    stock = models.PositiveIntegerField(null=True)
    image = models.ImageField(
        upload_to="product", verbose_name='Image')
    slug = models.SlugField(null=True, unique=True)
    active = models.BooleanField(default=True)
    hits = models.IntegerField(default=0)
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    def ImageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""

    def image_tag(self):
        return mark_safe('<img src="{}" heights="70" width="60" />'.format(self.image.url))
    image_tag.short_description = 'Image'
