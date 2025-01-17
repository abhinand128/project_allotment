from django.db import models
from django.contrib.auth.models import User

class Pathway(models.Model):
    pathway_id = models.AutoField(primary_key=True)
    pathway_name = models.CharField(max_length=50)

    def __str__(self):
        return self.pathway_name


class CourseType(models.Model):
    course_type_id = models.AutoField(primary_key=True)
    course_type_name = models.CharField(max_length=50)

    def __str__(self):
        return self.course_type_name


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_code = models.CharField(max_length=50)
    course_title = models.CharField(max_length=100)
    course_type = models.ForeignKey(CourseType, on_delete=models.CASCADE)
    credits = models.IntegerField()
    dept_id = models.CharField(max_length=50)
    strength = models.IntegerField()
    semester = models.IntegerField()

    def __str__(self):
        return self.course_title


class Student(models.Model):
    stud_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    stud_reg_no = models.CharField(max_length=50)
    stud_adm_no = models.CharField(max_length=50, unique=True)
    stud_roll_no = models.CharField(max_length=50)
    dob = models.DateField()
    pathway = models.ForeignKey(Pathway, on_delete=models.SET_NULL, null=True)
    department = models.CharField(max_length=100)
    normalized_marks = models.FloatField()

    def __str__(self):
        return self.student_name


class CourseAllotment(models.Model):
    stud_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    preference_no = models.IntegerField()

    def __str__(self):
        return f"{self.stud_id} -> {self.course_id}"

