from django.db import models


class Student(models.Model):
    name = models.CharField(
        max_length=100
    )

    active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(
        max_length=100
    )

    subject = models.CharField(
        max_length=100
    )

    active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(
        max_length=100
    )

    workload = models.PositiveIntegerField(
        default=0
    )

    teacher = models.ForeignKey(
        "Teacher",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Classroom(models.Model):
    name = models.CharField(
        max_length=100
    )

    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.year}"
