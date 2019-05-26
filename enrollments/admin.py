# Core imports
from django.contrib import admin

# Third party integration

# Apps imports
from enrollments.models import Enrollment, SchoolYear


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'grade', 'schollYear']


@admin.register(SchoolYear)
class SchoolYearAdmin(admin.ModelAdmin):
    list_display = ['id', 'star', 'finish']
