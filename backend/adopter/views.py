from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def views(req):
    return HttpResponse(" Health Check ")