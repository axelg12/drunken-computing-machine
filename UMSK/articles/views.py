from django.http import HttpResponse
from django.shortcuts import render

def getTeachers(request):
	return render(request, 'index.html')


# Create your views here.
