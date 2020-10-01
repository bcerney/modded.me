from django.db import models

# Create your models here.

class Quote(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    author = models.CharField(max_length=200, blank=True, default='')
    # TODO: add tags, reflections, added_by/user fields

    class Meta:
        ordering = ['created']