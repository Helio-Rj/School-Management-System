from django.shortcuts import render


def home(request):
    return render(request, "accounts/home.html")


def students(request):
    students_list = [
        "João",
        "Maria",
        "Carlos",
        "Fernanda",
        "Lucas",
    ]

    context = {
        "students": students_list
    }

    return render(
        request,
        "accounts/students.html",
        context
    )


def teachers(request):
    return render(request, "accounts/teachers.html")


def courses(request):
    return render(request, "accounts/courses.html")


def reports(request):
    return render(request, "accounts/reports.html")
