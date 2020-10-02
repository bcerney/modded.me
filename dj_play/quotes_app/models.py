from django.db import models

from taggit.managers import TaggableManager


class Quote(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    # TODO: research elements of ForeignKey
    owner = models.ForeignKey('auth.User', related_name='quotes', on_delete=models.CASCADE)
    text = models.TextField()
    author = models.CharField(max_length=200, blank=True, default='')
    tags = TaggableManager()

    class Meta:
        ordering = ['created']