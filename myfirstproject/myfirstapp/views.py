from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import *


# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Hello World")


def myfunctionabout(request):
    return HttpResponse("About Response")


def add(request, a, b):
    return HttpResponse(a+b)


def intro(request, name, age):
    mydictionary = {
        "name": name,
        "age": age
    }
    return JsonResponse(mydictionary)


def myfirstpage(request):
    return render(request, 'index.html')


def mysecondpage(request):
    return render(request, 'second.html')


def mythirdpage(request):
    var = "hello world"
    greeting = "hey how are you"
    fruits = ["apple", "mango", "banana"]
    num1, num2 = 3, 5
    ans = num1 > num2
    mydictionary = {
        "var": var,
        "msg": greeting,
        "myfruits": fruits,
        "num1": num1,
        "num2": num2,
        "ans": ans
    }
    return render(request, 'third.html', context=mydictionary)


def myimagepage(request):
    return render(request, 'imagepage.html')


def myimagepage2(request):
    return render(request, 'imagepage2.html')


def myimagepage3(request):
    return render(request, 'imagepage3.html')


def myimagepage4(request):
    return render(request, 'imagepage4.html')


def myform(request):
    return render(request, 'myform.html')


def submitmyform(request):
    mydictionary = {
        "val1": request.POST['mytext'],
        "val2": request.POST['mytextarea'],
        "method": request.method
    }
    return JsonResponse(mydictionary)


def myform2(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        form = FeedbackForm()
        mydictionary = {
            "form": form
        }
        return render(request, 'myform2.html', context=mydictionary)
