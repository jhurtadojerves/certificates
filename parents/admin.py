# Core imports
from django.contrib import admin

# Third party integration

# Apps imports
from parents.models import Parent


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ['id', 'identification_card', 'first_name', 'last_name']
    search_fields = ['identification_card', 'first_name', 'last_name']
