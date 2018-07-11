from django.db import models


class Student(models.Model):
    username = models.CharField(max_length=200)
