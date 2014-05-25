from django.db import models


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
	picture = models.FileField(upload_to='images/', default='images/default.png')
	caption = models.CharField(max_length=255, blank=True)
	publish_date = models.DateField()
	slot_number = IntegerRangeField(min_value=1, max_value=9)
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


