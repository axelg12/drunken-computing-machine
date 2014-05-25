from django.db import models


choices = [(i, i) for i in range(1, 10)]

# Create your models here.
class Image(models.Model):
	name = models.CharField(max_length=30)
	picture = models.FileField(upload_to='images/uploads', default='images/default.png')
	caption = models.CharField(max_length=255, blank=True)
	publish_date = models.DateField()
	slot_number = models.CharField(max_length=1, choices=choices, default=1)
	visible = models.BooleanField(default=True)

	def __unicode__(self):
		return self.name

class Teacher(models.Model):
	name = models.CharField(max_length=255)
	position = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)

	def __unicode__(self):
		return self.name

class Registration(models.Model):
	reg_date = models.CharField(max_length=255)
	reg_link = models.CharField(max_length=255)

	def __unicode__(self):
		return self.reg_date


