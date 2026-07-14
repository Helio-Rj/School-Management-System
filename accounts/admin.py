from django.contrib import admin
from .models import Student
from .models import Course
from .models import Teacher
from .models import Classroom

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Classroom)
