from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .models import Hobby, Project


def home(request):
    return render(request, "home.html")


def contact(request):
    return HttpResponse("<h1>Contact Me</h1>"
                        "Email: elijahcannon@mail.weber.edu")


def hobbies(request):
    context = {}
    context["dataset"] = Hobby.objects.all()
    return render(request, "hobbies.html", context)


def projects(request):
    context = {}
    context["dataset"] = Project.objects.all()
    return render(request, "projects.html", context)