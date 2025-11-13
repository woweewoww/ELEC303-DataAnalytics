from django.contrib import admin
from .models import TestingDatabase, Subject, Enrollment, Instructor, Student, FamilyInformation


admin.site.register(TestingDatabase)
admin.site.register(Subject)
admin.site.register(Enrollment)
admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(FamilyInformation)