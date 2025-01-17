from django.urls import path
from .views import student_login, course_selection

urlpatterns = [
    path('login/', student_login, name='student_login'),
    path('course_selection/', course_selection, name='course_selection'),
]
