from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=20)
    branch=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name

