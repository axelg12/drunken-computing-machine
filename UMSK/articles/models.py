# -*- coding: utf-8 -*-
from django.db import models
import os
#
#def get_file_path(instance, filename):
#    filename = "%s.%s" % (uuid.uuid4(), ext)
#    return os.path.join('uploads/logos', filename)

def update_filename(filename, slot):
    path = "UMSK/static/images/uploads/"
    ext = filename.split('.')[-1]
    format = 'someshit.'+ ext
    return os.path.join(path, format)

choices = [
		(1, '1. Bakgrunnur'), 
		(2, '2. Bakgrunnur'), 
		(3, '3. Bakgrunnur'), 
		(4, '1. lítil'), 
		(5, '2. lítil'), 
		(6, '3. lítil'), 
		(7, '4. lítil'), 
		(8, '5. lítil'), 
		(9, '6. lítil'), 
		(1, '7. lítil')
	]
choicesSmall = [
		(1, 'Mynd 1'), 
		(2, 'Mynd 2'), 
		(3, 'Mynd 3'), 
		(4, 'Mynd 4'), 
		(5, 'Mynd 5'), 
		(6, 'Mynd 6'), 
	]

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


# Create your models here.
class Image(models.Model):
	name = models.CharField(max_length=30)
	picture = models.FileField(upload_to='UMSK/static/images/uploads', default='static/images/default.png')
	caption = models.CharField(max_length=255, blank=True)
	publish_date = models.DateField()
	slot_number = IntegerRangeField(min_value=1, max_value=9, choices=choices)
	visible = models.BooleanField(default=True)

	def __unicode__(self):
		return self.name

class TextImage(models.Model):
	text = models.TextField(max_length=255)
	slot_number_text = IntegerRangeField(min_value=1, max_value=6, choices=choicesSmall)

class TextInformation(models.Model):
	text_info_id = models.CharField(max_length=50, choices=[
		('a','Hvað geri ég'),
		('b','Hver er ég'),
		('c','Verkefni')])
	text_info = models.TextField()

	def __unicode__(self):
		return self.name


class Registration(models.Model):
	reg_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name=u'Dagsetning við lok skráningar')
	reg_link = models.CharField(max_length=255, verbose_name=u'Slóð á skráningu (ekki gleyma http://)')

	def __unicode__(self):
		return str(self.reg_date) + ' - ' + self.reg_link


