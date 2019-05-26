# Core imports
from django.contrib import admin

# Third party integration

# Apps imports
from students.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'identification_card',
                    'first_name', 'last_name']
    search_fields = ['identification_card', 'first_name', 'last_name',
                     'parents__identification_card', 'parents__first_name',
                     'parents__last_name']
