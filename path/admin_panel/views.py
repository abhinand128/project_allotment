from django.shortcuts import render, redirect
from student.models import Student, CourseAllotment

def admin_dashboard(request):
    # View students, courses, and manage deadlines
    students = Student.objects.all()
    return render(request, 'admin_panel/dashboard.html', {'students': students})


def allocate_courses(request):
    # Allocation logic based on normalized marks
    return render(request, 'admin_panel/allocate_courses.html')
