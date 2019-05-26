# Core imports
from django.db import models

# Third party integration

# Apps imports
from enrollments.models import Enrollment


class Certificate(models.Model):
    enrollment = models.ForeignKey(
        Enrollment, on_delete=models.CASCADE, unique=True)
    creation = models.DateField(auto_now_add=True)

    def __str__(self):
        # {self.enrollments.student}, {self.enrollments.grade}
        return f"Certificado de promoción de "
