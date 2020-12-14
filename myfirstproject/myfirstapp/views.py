from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Hello World")


def myfunctionabout(request):
    return HttpResponse("About Response")


def add(request, a, b):
    return HttpResponse(a+b)
