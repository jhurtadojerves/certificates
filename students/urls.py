# Core imports
from django.urls import path

# Views imports
from students.views import StudentList

# URLs
app_name = 'Parent'

urlpatterns = [
    path('/', StudentList.as_view()),
]
