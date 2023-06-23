from django.http import HttpResponse


def index(request):
    return HttpResponse("please navigate to /portfolio")