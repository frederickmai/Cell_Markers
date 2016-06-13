from django.db import models
from django.core.urlresolvers import reverse

from .celltype import celltype
from .ablist import *
# Create your models here.
# MVC model view controller
# When ever models.py changes, run python manage.py makemigrations and then run python manage.py migrate


def upload_location(instance, filename):
	#filebase, extension = filename.split(".")
	#return "%s/%s.%s" %(instance.id, instance.id, extension)
	return "%s/%s" %(instance.id, filename)

class panel(models.Model):
	"""docstring for panel"""
	title = models.CharField(max_length = 120)
	# Usually title use charfield
	image = models.ImageField(upload_to=upload_location, 
			null=True, 
			blank=True, 
			width_field="width_field", 
			height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	description = models.TextField()
	# Usually main text use textfield

	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	cells = models.CharField(max_length=50, choices=celltype.cell_types())
	markers = models.CharField(max_length = 120, default=[display[1] for display in ablist.total_t_cell_list()], editable=True)

	def __unicode__ (self):
		return self.title

	def __str__ (self):
		return self.title

	def get_absolute_url(self):
		return reverse("panel:detail", kwargs={"id": self.id})

	class Meta:
		ordering = ["-timestamp", "-updated"]

# class antibody(object):
# 	"""docstring for antibody"""