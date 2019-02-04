from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

import datetime

class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    content = RichTextUploadingField()
    featured_image = models.ImageField(default = '')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title