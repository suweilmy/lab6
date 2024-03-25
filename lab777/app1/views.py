from django.shortcuts import render, redirect
from .models import Student, Course
from .forms import StudentForm, CourseForm


def students(request):
    students_list = Student.objects.all()
    student_form = StudentForm(request.POST or None)

    if request.method == 'POST' and student_form.is_valid():
        student_form.save()
        return redirect('students')

    context = {
        'students': students_list,
        'student_form': student_form,
    }
    return render(request, 'app1/students.html', context)


def courses(request):
    courses_list = Course.objects.all()
    course_form = CourseForm(request.POST or None)

    if request.method == 'POST' and course_form.is_valid():
        course_form.save()
        return redirect('courses')

    context = {
        'courses': courses_list,
        'course_form': course_form,
    }
    return render(request, 'app1/courses.html', context)


def details(request, student_id):
    student = Student.objects.get(id=student_id)
    available_courses = Course.objects.exclude(students=student)

    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        if course_id:
            student.courses.add(course_id)
            student.save()

    context = {
        'student': student,
        'available_courses': available_courses,
    }
    return render(request, 'app1/details.html', context)

