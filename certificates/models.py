# Core imports
from django.db import models

# Third party integration

# Apps imports
from grades.models import Grade
from students.models import Student


class Certificate(models.Model):
    #file = models.FileField()
    student = models.ForeignKey(
        Student, related_name="certificates", on_delete=models.CASCADE)
    grade = models.ForeignKey(
        Grade, related_name="certificates", on_delete=models.CASCADE)

    def __str__(self):
        return f"Certificado de promoción de {self.student}, {self.grade}"

    class Meta:
        unique_together = (('student', 'grade'))
