from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Image, Registration, update_filename, TextInformation


def index(request):
	images = Image.objects.filter(visible=True)

	for img in images:
		name = str(img.picture).split('/')[-1]
		img.picture = update_filename(name, img.slot_number)
		img.save()

	links = Registration.objects.first()

	texts = []
	for i in range(0,3):
		text = TextInformation.objects.filter(text_info_id=i).last()
		texts.append(text)
		
	caption = None

	return render(request, 'index.html', {'images': images, 'link': links})