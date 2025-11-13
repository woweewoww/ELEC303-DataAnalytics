from django import forms
from .models import Subject, Enrollment, Instructor, Student, FamilyInformation

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = '__all__'

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class FamilyInformationForm(forms.ModelForm):
    class Meta:
        model = FamilyInformation
        fields = '__all__'