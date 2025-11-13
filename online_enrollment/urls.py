from django.urls import path
from . import views

urlpatterns = [
    path('subjects/', views.subject, name='subject'),
    path('enrollment/', views.enrollment, name='enrollment'),
    path('instructor/', views.instructor, name='instructor'),
    path('student/', views.student, name='student'),
    path('fam_info/', views.fam_info, name='fam_info'),
    path('success/', views.success, name='success')
]