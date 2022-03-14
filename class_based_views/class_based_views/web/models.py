from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    NAME_MAX_LENGTH = 25
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    def __str__(self):
        return self.name


class Todo(models.Model):
    CHOICES = [(x, x) for x in ('High', 'Medium', 'Low')]
    TITLE_MAX_LENGTH = 25
    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    description = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    urgency = models.CharField(
        max_length=6,
        choices=CHOICES,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title
