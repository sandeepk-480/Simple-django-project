from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    roll = models.IntegerField(unique=True, null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name