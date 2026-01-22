# Quick Start Guide

## Get Started in 5 Minutes

### 1. Clone the Repository
```bash
git clone https://github.com/MahmoudAlmodalal/my-course-repo.git
cd my-course-repo
```

### 2. Set Up Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Initialize Database
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 4. Run Server
```bash
python manage.py runserver
```

### 5. Access Application
- **Frontend**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin

---

## Create Test Data

### Via Admin Panel (Easiest)

1. Go to http://localhost:8000/admin
2. Login with superuser credentials
3. Click "Add Course"
4. Fill in course details
5. Click "Add another Question" in the Questions section
6. Add questions with choices
7. Mark correct choices with the checkbox

### Via Django Shell (Advanced)

```bash
python manage.py shell

from onlinecourse.models import Course, Question, Choice
from django.utils import timezone

# Create course
course = Course.objects.create(
    name="Python Basics",
    description="Learn Python fundamentals",
    pub_date=timezone.now().date()
)

# Create question
question = Question.objects.create(
    course=course,
    text="What is Python?",
    grade=10
)

# Create choices
Choice.objects.create(question=question, text="A programming language", is_correct=True)
Choice.objects.create(question=question, text="A snake", is_correct=False)
Choice.objects.create(question=question, text="A type of food", is_correct=False)
```

---

## Test the Exam Feature

1. **Register** a new user
2. **Enroll** in the course
3. **Click "Start Exam"**
4. **Select answers** (checkboxes)
5. **Click "Submit"**
6. **View results** with detailed feedback

---

## Key Files

| File | Purpose |
| --- | --- |
| `onlinecourse/models.py` | Database models (Question, Choice, Submission) |
| `onlinecourse/views.py` | View logic (submit, show_exam_result) |
| `onlinecourse/admin.py` | Admin configuration |
| `onlinecourse/templates/course_detail_bootstrap.html` | Exam form |
| `onlinecourse/templates/exam_result_bootstrap.html` | Results page |
| `SOLUTION_README.md` | Comprehensive documentation |
| `IMPLEMENTATION_GUIDE.md` | Detailed code explanations |

---

## Common Commands

```bash
# Run development server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Access Django shell
python manage.py shell

# Create superuser
python manage.py createsuperuser

# Collect static files (for production)
python manage.py collectstatic
```

---

## Grading System

- **Pass**: Score ≥ 80%
- **Fail**: Score < 80%
- **Score Calculation**: (Correct Points / Total Points) × 100

### Correct Answer Logic
A question is marked correct only if:
- ✓ ALL correct choices are selected
- ✓ NO incorrect choices are selected

---

## Troubleshooting

### Database Error
```bash
python manage.py migrate
```

### No Questions Showing
1. Go to admin panel
2. Add questions to the course
3. Add choices to each question

### Import Error
```bash
pip install -r requirements.txt
```

### Port Already in Use
```bash
python manage.py runserver 8001
```

---

## Next Steps

1. Read `SOLUTION_README.md` for full documentation
2. Read `IMPLEMENTATION_GUIDE.md` for code details
3. Customize templates to match your branding
4. Deploy to production
5. Add more features (timers, analytics, etc.)

---

## Support

- **Django Docs**: https://docs.djangoproject.com/
- **GitHub Issues**: Open an issue in the repository
- **Django Community**: https://www.djangoproject.com/community/

---

**Ready to go!** 🚀
