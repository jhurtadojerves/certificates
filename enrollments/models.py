# Core imports
from django.db import models

# Third party integration

# Locals apps import
from students.models import Student
from grades.models import Grade


class SchoolYear(models.Model):
    star = models.DateField()
    finish = models.DateField()


class Enrollment(models.Model):
    student = models.ForeignKey(
        Student, related_name="enrollments", on_delete=models.CASCADE)
    grade = models.ForeignKey(
        Grade, related_name="enrollments", on_delete=models.CASCADE)
    schollYear = models.ForeignKey(
        SchoolYear, related_name='enrollments', on_delete=models.CASCADE)

    def __str__(self):
        return f'Matrícula de {self.student}, {self.grade}'
