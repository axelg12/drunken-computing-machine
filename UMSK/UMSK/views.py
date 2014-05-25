from django.http import HttpResponse
from articles import Image


def index():
	images = Image.objects.filter(visible=True)
	visible_images = []
	used_slots = []
	for img in images:
		if img.slot_number not in used_slots:
			
	return render(request, 'index.html', {'images': images})