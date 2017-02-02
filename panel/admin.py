from django.contrib import admin

# Register your models here.
from .models import panel
from .models import SignUp
from .forms import SignUpForm


class facsModelAdmin(admin.ModelAdmin):
	"""Google Model Admin to know more"""
	list_display = ["title", "cells", "markers", "updated", "timestamp",]
	list_filter = ["cells", "updated"] # Want markers filtered later
	list_display_links = ["cells"]
	list_editable = ["title"]
	search_fields = ["title", "cells", "updated"] # allow all fields to be searched except credentials?
	class Meta:
		"""docstring for ClassName"""
		model = panel

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "updated"]
	form = SignUpForm
# 	class Meta:
# 		model = SignUp

admin.site.register(panel, facsModelAdmin)
#Register model "panel" in admin site
admin.site.register(SignUp)
