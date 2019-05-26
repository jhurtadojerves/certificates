# Core imports
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

# Local imports
from students.models import Student


class StudentList(ListView):
    model = Student
    template = 'students/student_list.html'
    context_object_name = 'students'


class StudentCreate(CreateView):
    model = Student
