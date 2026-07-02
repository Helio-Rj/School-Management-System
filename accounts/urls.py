from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("students/", views.students, name="students"),
    path("teachers/", views.teachers, name="teachers"),
    path("courses/", views.courses, name="courses"),
    path("reports/", views.reports, name="reports"),
]