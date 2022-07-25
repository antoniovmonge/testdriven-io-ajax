from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Todo(models.Model):
    task = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, blank=True, null=True, unique=True)

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        return reverse("todo",  args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.task)
        super().save(*args, **kwargs)
