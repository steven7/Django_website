from django.shortcuts import render
from django.urls import resolve
from django.test import TestCase
from django.http import HttpResponse

# Create your views here.
def home_page(request):
	return HttpResponse('<html><title>To-Do lists</title></html>')