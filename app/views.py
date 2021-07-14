from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hey, Its my first django app.")

