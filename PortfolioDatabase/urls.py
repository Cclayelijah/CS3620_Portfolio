from django.urls import path

from PortfolioDatabase import views

app_name = 'PortfolioDatabase'


urlpatterns = [
    path('', views.home, name="home"),
    path('hobbies/', views.hobbies, name="hobbies"),
    path('projects/', views.projects, name="projects"),
    path('contact/', views.contact, name="contact"),
    path('hobbies/<int:hobby_id>', views.hobby, name="hobby"),
    path('projects/<int:project_id>', views.project, name="project"),
]

