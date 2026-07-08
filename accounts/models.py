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


class Course(models.Model):
    name = models.CharField(
        max_length=100
    )

    workload = models.PositiveIntegerField(
        default=0
    )

    def __str__(self):
        return self.name
