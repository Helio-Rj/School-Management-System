from django.shortcuts import render

from .models import Student, Course,Teacher


def home(request):
    return render(request, "accounts/home.html")


def students(request):
    students_list = Student.objects.all()

    context = {
        "students": students_list,
        "page_title": "Students",
        "school_name": "School Management System",
        "total_students": students_list.count(),

    }

    return render(
        request,
        "accounts/students.html",
        context
    )


def teachers(request):
    teachers_list = Teacher.objects.all()

    context = {
        "teachers": teachers_list,
        "page_title": "Teachers",
        "school_name": "School Management System",
        "total_teachers": teachers_list.count(),
    }

    return render(
        request,
        "accounts/teachers.html",
        context
    )


def courses(request):
    courses_list = Course.objects.all()

    context = {
        "courses": courses_list,
        "page_title": "Courses",
        "total_courses": courses_list.count(),
    }

    return render(request, "accounts/courses.html", context)


def reports(request):
    return render(request, "accounts/reports.html")
