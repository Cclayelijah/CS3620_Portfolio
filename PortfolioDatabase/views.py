from django.shortcuts import render
from django.http import HttpResponse

from .models import Hobby, Project


def home(request):
    return HttpResponse(""
                        "<h1>Home</h1>"
                        "<p>Hi!<br />My name is Elijah Cannon and I am a senior at Weber State University studying computer science :) Please check out my hobbies and also the cool projects I have been working on.</p>")


def contact(request):
    return HttpResponse("<h1>Contact Me</h1>"
                        "Email: elijahcannon@mail.weber.edu")


def hobbies(request):
    hobby_list = Hobby.objects.all()
    return HttpResponse("<h1>My Hobbies</h1>" + str(hobby_list))


def projects(request):
    project_list = Project.objects.all()
    return HttpResponse("<h1>My Projects</h1>" + str(project_list))