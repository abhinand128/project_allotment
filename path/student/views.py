from django.shortcuts import render, redirect
from .models import Student, Course, Pathway, CourseAllotment
from .forms import LoginForm, CourseSelectionForm

def student_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            adm_no = form.cleaned_data['stud_adm_no']
            dob = form.cleaned_data['dob']
            try:
                student = Student.objects.get(stud_adm_no=adm_no, dob=dob)
                request.session['student_id'] = student.stud_id
                return redirect('course_selection')
            except Student.DoesNotExist:
                return render(request, 'student/login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = LoginForm()
    return render(request, 'student/login.html', {'form': form})


def course_selection(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('student_login')

    student = Student.objects.get(stud_id=student_id)
    if request.method == "POST":
        form = CourseSelectionForm(request.POST)
        if form.is_valid():
            # Save course preferences logic here
            return redirect('success')
    else:
        form = CourseSelectionForm()

    # Filter courses based on the pathway
    pathway = student.pathway
    courses = Course.objects.filter(course_type__course_type_name="DSC")
    context = {'form': form, 'student': student, 'courses': courses}
    return render(request, 'student/course_selection.html', context)
