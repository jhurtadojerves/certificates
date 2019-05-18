# Core imports
from django.contrib import admin

# Third party integration

# Apps imports
from certificates.models import Certificate


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'grade']
    search_fields = ['student__first_name',
                     'student__last_name', 'student__identification_card']
