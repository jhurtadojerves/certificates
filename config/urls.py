# Core imports
from django.contrib import admin
from django.urls import path, include

# URLs
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('students', include('students.urls'))
]
