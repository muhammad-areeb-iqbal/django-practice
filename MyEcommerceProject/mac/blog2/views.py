from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Blog 2 Index Url")