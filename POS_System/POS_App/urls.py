from django.urls import path, include
from .import views

urlpatterns = [
    path('', include('POS_System.urls')),
    path('register/', views.register, name='register'),
    path('login/', views.Login_view, name='login'),
    path('logout/', views.logout_view, name='login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),  # Specific path for admin dashboard
    path('staff-dashboard/', views.staff_dashboard, name='staff_dashboard'),
]