from django.http import HttpResponse
from django.shortcuts import render
from articles.models import *

def getTeachers(request):
	teachers = teacher.objects.all().order_by('name')
	return render(request, 'teacherTemp.html', {'teachers': teachers})


# Create your views here.
