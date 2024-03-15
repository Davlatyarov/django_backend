from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('booking/<int:id>', views.booking, name='booking'),
    path('doctors/', views.doctors, name='doctors'),
    path('num_user/', views.num_user, name='num_user'),
]
