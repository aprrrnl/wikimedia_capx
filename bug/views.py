from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello. Welcome to the bug app 😟")
