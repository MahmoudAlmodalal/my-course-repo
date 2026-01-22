from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    # Index page showing the list of courses
    path(route='', view=views.CourseListView.as_view(), name='index'),
    
    # Authentication routes
    path('registration/', views.registration_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    
    # Course detail view (where lessons and the exam are displayed)
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),
    
    # Enrollment route
    path('<int:course_id>/enroll/', views.enroll, name='enroll'),

    # <HINT> Requirement: Route for submitting the exam
    path('<int:course_id>/submit/', views.submit, name='submit'),
    
    # <HINT> Requirement: Route for showing the exam result
    path('<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name='show_exam_result'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
