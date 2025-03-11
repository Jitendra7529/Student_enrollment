from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .models import Student, Course, Enrollment
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from .forms import StudentForm, CourseForm, EnrollmentForm

# Create your views here.

class HomepageView(TemplateView):
    template_name = 'homepage.html'

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'
    context_object_name = 'student'


class StudentCreateView(CreateView):
    model = Student
    template_name = 'student_form.html'
    form_class = StudentForm
    success_url = reverse_lazy('student_list')  # Redirect to the student list after creation


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student_form.html'
    form_class = StudentForm
    success_url = reverse_lazy('student_list')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('student_list')


# Course View

class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'
    context_object_name = 'course'

class CourseCreateView(CreateView):
    model = Course
    template_name = 'course_form.html'
    form_class = CourseForm
    success_url = reverse_lazy('course_list')  # Redirect to the course list after creation

    

class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'course_form.html'
    form_class = CourseForm
    success_url = reverse_lazy('course_list')

    

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'course_confirm_delete.html'
    success_url = reverse_lazy('course_list')

    

# Enrollment Views
class EnrollmentCreateView(CreateView):
    model = Enrollment
    template_name = 'enrollment_form.html'
    form_class = EnrollmentForm
    success_url = reverse_lazy('student_list')  # Redirect to the student list after enrollment

class EnrollmentUpdateView(UpdateView):
    model = Enrollment
    template_name = 'enrollment_form.html'
    form_class = EnrollmentForm
    success_url = reverse_lazy('student_list')

class EnrollmentDeleteView(DeleteView):
    model = Enrollment
    template_name = 'enrollment_confirm_delete.html'
    success_url = reverse_lazy('student_list')


