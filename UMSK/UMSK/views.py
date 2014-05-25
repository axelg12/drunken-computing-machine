from django.http import HttpResponse
from articles import Image


def index():
	images = Image.objects.all()
	return render(request, 'index.html', {'images': images})