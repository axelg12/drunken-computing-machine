from django.db import models


choices = [(i, i) for i in range(1, 10)]

# Create your models here.
class Image(models.Model):
	name = models.CharField(max_length=30)
	picture = models.FileField(upload_to='images/uploads', default='images/default.png')
	caption = models.CharField(max_length=255, blank=True)
	publish_date = models.DateField()
	slot_number = IntegerRangeField(min_value=1, max_value=9, choices=[
		(1, '1. Bakgrunnur'), 
		(2, '2. Bakgrunnur'), 
		(3, '3. Bakgrunnur'), 
		(4, '1. lítil'), 
		(5, '2. lítil'), 
		(6, '3. lítil'), 
		(7, '4. lítil'), 
		(8, '5. lítil'), 
		(9, '6. lítil'), 
		(1, '7. lítil')])
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


