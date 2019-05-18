# Core imports
from django.db import models

# Third party integration


class Grade(models.Model):

    name = models.CharField(max_length=128)
    parallel = models.CharField(max_length=1, default="A")

    def __str__(self):
        return f"{self.name} paralelo {self.parallel}"

    class Meta:
        unique_together = (('name', 'parallel'))
