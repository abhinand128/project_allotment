from django.urls import path
from .views import admin_dashboard, allocate_courses

urlpatterns = [
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('allocate/', allocate_courses, name='allocate_courses'),
]
