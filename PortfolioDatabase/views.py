from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .models import Hobby, Project


def home(request):
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")


def hobbies(request):
    context = {}
    context["dataset"] = Hobby.objects.all()
    return render(request, "hobbies.html", context)


def hobby(request, hobby_id):
    context = {}
    context["dataset"] = Hobby.objects.get(pk=hobby_id)
    return render(request, "hobby.html", context)


def projects(request):
    context = {}
    context["dataset"] = Project.objects.all()
    return render(request, "projects.html", context)


def project(request, project_id):
    context = {}
    context["dataset"] = Project.objects.get(pk=project_id)
    return render(request, "project.html", context)