from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Image, Registration, update_filename, TextInformation, TextImage


def index(request):
	images = Image.objects.filter(visible=True)

	for img in images:
		name = str(img.picture).split('/')[-1]
		img.picture = update_filename(name, img.slot_number)
		img.save()

	links = Registration.objects.first()

	text1 = TextInformation.objects.filter(text_info_id='a').last()
	text2 = TextInformation.objects.filter(text_info_id='b').last()
	text3 = TextInformation.objects.filter(text_info_id='c').last()

	caption1 = Image.objects.filter(slot_number=4).last()
	caption2 = Image.objects.filter(slot_number=5).last()
	caption3 = Image.objects.filter(slot_number=6).last()
	caption4 = Image.objects.filter(slot_number=7).last()
	caption5 = Image.objects.filter(slot_number=8).last()
	caption6 = Image.objects.filter(slot_number=9).last()

	return render(request, 'index.html', {'images': images, 'link': links, 'text1': text1, 'text2': text2, 'text3': text3, 'caption1': caption1, 'caption2': caption2, 'caption3': caption3, 'caption4': caption4, 'caption5': caption5, 'caption6': caption6 })
