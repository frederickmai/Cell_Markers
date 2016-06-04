from django.db import models
from django.core.urlresolvers import reverse

from .celltype import celltype
from .ablist import *
# Create your models here.
# MVC model view controller

class panel(models.Model):
	"""docstring for panel"""
	title = models.CharField(max_length = 120)
	# Usually title use charfield
	description = models.TextField()
	# Usually main text use textfield

	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	cells = models.CharField(max_length=50, choices=celltype.cell_types(), default='T Cell')
	markers = models.CharField(max_length = 120, default=[display[1] for display in ablist.total_t_cell_list()], editable=True)

	def __unicode__ (self):
		return self.title

	def __str__ (self):
		return self.title

	def get_absolute_url(self):
		return reverse("panel:detail", kwargs={"id": self.id})

# class antibody(object):
# 	"""docstring for antibody"""