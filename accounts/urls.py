from django.urls import path
from .import views
from .views import HomepageView
# from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),  # Root path routed to homepage view 
    # path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', LogoutView.as_view(next_page='homepage'), name='logout'),
    # path('profile/', ProfileView.as_view(), name='profile'),
    path('students/', views.StudentListView.as_view(), name='student_list'),  # as_view() method is used to differentiate a class based view from function based view.
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('student/new/', views.StudentCreateView.as_view(), name='student_create'),
    path('student/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student_update'),
    path('student/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
    # path('accounts/profile/', MarksListView.as_view()),
    
    # Course URLs
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('course/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('course/new/', views.CourseCreateView.as_view(), name='course_create'),
    path('course/<int:pk>/edit/', views.CourseUpdateView.as_view(), name='course_update'),
    path('course/<int:pk>/delete/', views.CourseDeleteView.as_view(), name='course_delete'),

    # Enrollment URLs
    path('enrollment/new/', views.EnrollmentCreateView.as_view(), name='enrollment_create'),
    path('enrollment/<int:pk>/edit/', views.EnrollmentUpdateView.as_view(), name='enrollment_update'),
    path('enrollment/<int:pk>/delete/', views.EnrollmentDeleteView.as_view(), name='enrollment_delete'),
]
