# Core imports
from django.contrib import admin

# Third party integration

# Apps imports
from grades.models import Grade


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parallel']
