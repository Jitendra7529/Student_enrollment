# Student Enrollment System

A comprehensive web application built with Django for managing student enrollments, courses, and academic records.

## Features

- **Student Management**: Add, view, edit, and delete student records
- **Course Management**: Create and manage course offerings with descriptions and credit information
- **Enrollment System**: Enroll students in courses and track their academic progress
- **Modern UI**: Clean, responsive interface built with custom CSS
- **Data Validation**: Form validation to ensure data integrity

## Technology Stack

- **Backend**: Django 5.1
- **Database**: SQLite (default)
- **Frontend**: HTML, CSS, Django Templates
- **Deployment**: Ready for deployment on any Django-compatible hosting

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/student-enrollment-system.git
   cd student-enrollment-system
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (admin):
   ```bash
   python manage.py createsuperuser
   ```

6. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

8. Access the application at http://127.0.0.1:8000/

## Usage

### Student Management

- **View Students**: Navigate to the Students section to see all registered students
- **Add Student**: Use the "Add New Student" button to create a new student record
- **Student Details**: Click on a student to view their complete profile and course enrollments
- **Edit/Delete**: Options to modify or remove student records as needed

### Course Management

- **View Courses**: Browse all available courses with their credit information
- **Add Course**: Create new courses with descriptions and credit values
- **Course Details**: View detailed information about each course and enrolled students

### Enrollment Management

- **Enroll Students**: Easily enroll students in available courses
- **Track Enrollments**: View and manage all enrollments from student profiles
- **Remove Enrollments**: Option to drop students from courses when needed

## Project Structure

```
student-enrollment-system/
├── accounts/                  # Main application
│   ├── migrations/            # Database migrations
│   ├── static/                # Static files (CSS, JS)
│   │   └── css/
│   │       └── style.css      # Custom styling
│   ├── templates/             # HTML templates
│   ├── admin.py               # Admin configuration
│   ├── forms.py               # Form definitions
│   ├── models.py              # Data models
│   ├── urls.py                # URL routing
│   └── views.py               # View controllers
├── coreproject/               # Project settings
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL routing
│   └── wsgi.py                # WSGI configuration
├── static/                    # Collected static files
├── staticfiles/               # Production static files
├── manage.py                  # Django management script
└── requirements.txt           # Project dependencies
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## Acknowledgments

- Django documentation and community
- Bootstrap for design inspiration
- All contributors who have helped improve this project

