from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Image


def index(request):
	images = Image.objects.filter(visible=True)
	visible_images = []
	used_slots = []
	for img in images:
		if img.slot_number not in used_slots:
			used_slots.append(img.slot_number)
			visible_images.append(img)

	visible_images = sorted(visible_images, key=lambda image: image.slot_number)
	for img in visible_images:
		img.picture = str(img.picture).strip('UMSK/')

	return render(request, 'index.html', {'images': visible_images})