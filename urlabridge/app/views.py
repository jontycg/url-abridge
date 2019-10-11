from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the url-abridge index.")


def redirect(request, path):
    return HttpResponse("Hello there, your path is {}".format(path))
