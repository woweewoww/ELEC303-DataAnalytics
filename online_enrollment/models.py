from django.db import models

class TestingDatabase(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    registration_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.first_name}"
    
class Subject(models.Model):
    subject_code = models.CharField(max_length=10)
    time = models.CharField()
    day = models.CharField(max_length=10)
    unit = models.IntegerField()
    room = models.CharField(max_length=10)

    def __str__(Subject):
        return f"{Subject.subject_code}"

    
class Enrollment(models.Model):
    stud_id = models.CharField()
    course = models.CharField(max_length=100)
    subject_code = models.CharField()
    school_year = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    def __str__(Enrollment):
        return f"{Enrollment.stud_id}"

class Instructor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact_no = models.CharField()
    department = models.CharField(max_length=100)

    def __str__(Instructor):
        return f"{Instructor.first_name}"

class Student(models.Model):
    stud_id = models.CharField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_no = models.CharField()
    email = models.EmailField(max_length=100)

    def __str__(Student):
        return f"{Student.first_name}"
    
class FamilyInformation(models.Model):
    fathers_name = models.CharField(max_length=100)
    mothers_name = models.CharField(max_length=100)
    contact_no = models.CharField()
    address = models.CharField(max_length=100)
    guardian = models.CharField(max_length=100)

    def __str__(FamilyInformation):
        return f"{FamilyInformation.fathers_name}"
    




    

