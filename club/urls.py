from django.contrib import admin
from django.urls import path, include
from club import views

urlpatterns = [
    path('', views.main_home, name='main_home'),
    path('<int:club_type>/', views.main_type, name='main_type'),
    path('post/<int:club_id>/', include('post.urls')),
]
