from django.db import models

# Create your models here.
class image(models.Model):
	name = models.CharField(max_length=30)
	picture = models.FileField(upload_to='UMSK/Big Picture', default='images/default.png')
	caption = models.CharField(max_length=255, blank=True)
	publish_date = models.DateField()

	def __unicode__(self):
		return self.name

class teacher(models.Model):
	name = models.CharField(max_length=255)
	position = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)

	def __unicode__(self):
		return self.name

class registration(models.Model):
	reg_date = models.CharField(max_length=255)
	reg_link = models.CharField(max_length=255)

	def __unicode__(self):
		return self.reg_date


