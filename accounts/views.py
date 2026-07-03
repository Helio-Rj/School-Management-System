from django.shortcuts import render


def home(request):
    return render(request, "accounts/home.html")


def students(request):
    students_list = [
        {
            "name": "João",
            "active": True,
        },
        {
            "name": "Maria",
            "active": False,
        },
        {
            "name": "Carlos",
            "active": True,
        },
        {
            "name": "Fernanda",
            "active": True,
        },
        {
            "name": "Lucas",
            "active": False,
        },
        {
            "name": "Helena",
            "active": True,
        },
    ]

    context = {
        "students": students_list,
        "page_title": "Students",
        "school_name": "School Management System",
        "total_students": len(students_list),

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
