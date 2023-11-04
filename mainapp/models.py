from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=10, unique=True)
    marks_hindi = models.IntegerField()
    marks_english = models.IntegerField()
    marks_math = models.IntegerField()
    marks_science = models.IntegerField()
    marks_grography = models.IntegerField()
    photo = models.ImageField(upload_to='media/student_photos/')
    class_level = models.IntegerField()

    def __str__(self):
        return self.name
