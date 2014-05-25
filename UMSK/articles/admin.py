from django.contrib import admin

from articles.models import Image, TextInformation, Registration

admin.site.register(Image)
admin.site.register(TextInformation)
admin.site.register(Registration)
