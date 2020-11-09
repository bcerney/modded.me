# from django.db import models

# from taggit.managers import TaggableManager


# class Quote(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     # TODO: https://stackoverflow.com/questions/2886987/adding-custom-fields-to-users-in-django
#     user = models.ForeignKey('settings.AUTH_USER_MODEL', related_name='quotes', on_delete=models.CASCADE)
#     text = models.TextField()
#     author = models.CharField(max_length=200, blank=True, default='')
#     tags = TaggableManager()

#     def __str__(self):
#         return f'"{self.text}" - {self.author}'

#     class Meta:
#         ordering = ['created']


# class Reflection(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     user = models.ForeignKey('settings.AUTH_USER_MODEL', related_name='reflections', on_delete=models.CASCADE)
#     quote = models.ForeignKey('Quote', related_name='+', on_delete=models.CASCADE)
#     # TODO: confirm attributes of TextField, good fit?
#     text = models.TextField()

#     def __str__(self):
#         return f'{self.quote} | {self.text}'

#     class Meta:
#         ordering = ['created']
