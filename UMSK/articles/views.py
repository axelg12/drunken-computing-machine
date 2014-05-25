from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Teacher

def getTeachers(request):
	teachers = Teacher.objects.all().order_by('name')
	return render(request, 'index.html', {'teachers': teachers})


# Create your views here.
