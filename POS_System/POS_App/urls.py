from django.urls import path
from .import views

urlpatterns = [
    path('', views.lobby, name='lobby'),
    path('register/', views.register, name='register'),
    path('login/', views.Login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('seller-dashboard/', views.seller_dashboard, name='seller_dashboard'),
]
