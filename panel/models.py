from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify

from .celltype import celltype
from .ablist import *
# Create your models here.
# MVC model view controller
# When ever models.py changes, run python manage.py makemigrations and then run python manage.py migrate

#panel.objects.all() is a type of model manager too
#panel.objects.create(user=user, title="some title") creates instance itself
class panel_manager(models.Manager):
	def active(self, *args, **kwargs):
		# panel.objects.all() = super(panel_manager, self.all())
		return super(panel_manager, self).filter(draft=False)#.filter(publish__lte=timezone.now())
	
def upload_location(instance, filename):
	#filebase, extension = filename.split(".")
	#return "%s/%s.%s" %(instance.id, instance.id, extension)
	return "%s/%s" %(instance.id, filename)

class panel(models.Model):
	"""docstring for panel"""
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length = 120)
	# Usually title use charfield
	slug = models.SlugField(unique=True)
	image = models.ImageField(upload_to=upload_location, 
			null=True, 
			blank=True, 
			width_field="width_field", 
			height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	description = models.TextField()
	# Usually main text use textfield
	draft = models.BooleanField(default=False)
	publish = models.DateField(auto_now=False, auto_now_add=False)

	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	
	objects = panel_manager()
	
	cells = models.CharField(max_length=50, choices=celltype.cell_types())
	markers = models.CharField(max_length = 120, default=[display[1] for display in ablist.total_t_cell_list()], editable=True)

	def __unicode__ (self):
		return self.title

	def __str__ (self):
		return self.title

	def get_absolute_url(self):
		return reverse("panel:detail", kwargs={"slug": self.slug})

	class Meta:
		ordering = ["-timestamp", "-updated"]


def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = panel.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_panel_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_panel_receiver, sender=panel)
# class antibody(object):
# 	"""docstring for antibody"""