from django.shortcuts import render, redirect
from .forms import SubjectForm, EnrollmentForm, Instructor, Student, FamilyInformation
# from django.http import HttpResponse
# from django.views import View
# from .models import *

def subject(request):
    #subject = Subject.objects.all()
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SubjectForm('form.html', {'form': form, 'level': subject})
    return render(request, 'subjects.html', {'subjects' : subject})

def enrollment(request):
    #enrollment = Enrollment.objects.all()
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success') 

    return render(request, 'enrollment.html', {'enrollment' : enrollment})

def instructor(request):
    instructor = Instructor.objects.all()

    return render(request, 'instructor.html', {'instructor' : instructor})

def student(request):
    student = Student.objects.all()

    return render(request, 'student.html', {'student' : student})

def fam_info(request):
    fam_info = FamilyInformation.objects.all()

    return render(request, 'FamilyInformation.html', {'FamilyInformation' : fam_info})

def success(request):
    return render(request, 'success.html')