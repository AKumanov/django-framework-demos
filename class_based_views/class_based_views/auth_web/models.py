from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()

#
# class Profile(models.Model):
#     NAME_MAX_LENGTH = 30
#     first_name = models.CharField(
#         max_length=NAME_MAX_LENGTH
#     )
#     last_name = models.CharField(
#         max_length=NAME_MAX_LENGTH
#     )
#
#     email = models.CharField(
#         max_length=200
#     )
#
#     user = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#
#     @property
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
#     def __str__(self):
#         return self.full_name
