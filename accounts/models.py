from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)  # Increase max_length for email
    phone = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Course(models.Model):
    name = models.CharField(max_length=100)  # Increase max_length for course name
    description = models.TextField()
    credits = models.PositiveIntegerField()  # Number of credit for the course.

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Correct the field name to lowercase
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # ForeignKey to Course
    enrollment_date = models.DateTimeField(auto_now_add=True)  # Defines the date in which the student is enrolled 

    def __str__(self):
        return f"{self.student} enrolled in {self.course}"
    


    

# class Marks(models.Model):
#     enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
#     subject = models.CharField(max_length=100)   # useful if student takes the multiple course
#     marks_obtained = models.PositiveIntegerField()
#     graded_by = models.CharField(max_length=30)
#     data_recorded = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = "marks" 

#     def __str__(self):
#        return f"{self.enrollment} - {self.enrollment.course}: {self.marks_obtained}"
