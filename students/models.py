# Core imports
from django.db import models

# Third party integration

# Apps imports
from parents.models import Parent


class Student(models.Model):
    identification_card = models.CharField(
        max_length=11, null=True, default=None, unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    parents = models.ManyToManyField(Parent, related_name='students')

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
