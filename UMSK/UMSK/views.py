from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Image, Registration, update_filename


def index(request):
	images = Image.objects.filter(visible=True)

	for img in images:
		name = str(img.picture).split('/')[-1]
		img.picture = update_filename(name, img.slot_number)
		img.save()

	links = Registration.objects.first()

	
	text = TextInformation.objects.all()

	for t in text:
		delete_existing_text(t.text_info_id)


	caption = None

	return render(request, 'index.html', {'images': images, 'link': links})