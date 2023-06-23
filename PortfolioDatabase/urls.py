from django.urls import path

from PortfolioDatabase import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('hobbies/', views.hobbies, name="hobbies"),
    path('projects/', views.projects, name="projects")
]
